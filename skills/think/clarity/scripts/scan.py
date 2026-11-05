#!/usr/bin/env python3
"""Clarity scanner for slides, memos and messages. Stdlib only.

Usage:  python3 scan.py FILE [--lang en|de] [--json] [--known "Term A,Term B"]
        cat FILE | python3 scan.py [--lang en|de] [--json]

Prints the titles as a storyline, a concept chart of unfamiliar terms, the
worst sentences, AI filler, and a load number for comparing drafts.
Single flags are hints; clusters are problems.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
LANG = "en"

# ------------------------------------------------------------------ data
def read_list(name):
    path = DATA / name
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [ln.rstrip("\n") for ln in fh if ln.strip() and not ln.startswith("#")]


FUNC_WORDS = {"en": "the and of to is in that for with are on this we you it as".split(),
              "de": "der die und das ist nicht mit für von zu den dem ein eine wir sie auf".split()}


def detect_lang(text):
    counts = Counter(re.findall(r"[a-zäöüß]+", text.lower()))
    score = {lang: sum(counts[w] for w in words) for lang, words in FUNC_WORDS.items()}
    return "de" if score["de"] > score["en"] else "en"


# ------------------------------------------------------------- markdown
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
BULLET = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+(.*)$")
HR = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE = [(r"!\[[^\]]*\]\([^)]*\)", ""), (r"\[\[([^\]|]+)(\|[^\]]*)?\]\]", r"\1"),
          (r"\[([^\]]+)\]\([^)]*\)", r"\1"), (r"<[^>]+>", ""), (r"https?://\S+", ""),
          (r"`[^`]*`", ""), (r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1", r"\2"), (r"^>\s?", "")]
ABBR = ["e.g.", "i.e.", "etc.", "vs.", "cf.", "Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Inc.", "Ltd.", "No.",
        "Fig.", "approx.", "St.", "Jr.", "Sr.", "z. B.", "z.B.", "bzw.", "usw.", "u. a.", "u.a.", "d. h.",
        "d.h.", "ggf.", "ca.", "Nr.", "inkl.", "exkl.", "evtl.", "sog.", "Mio.", "Mrd.", "Tsd.", "Std.",
        "Min.", "Abs.", "Art.", "vgl.", "o. ä.", "o.ä.", "u. U.", "max.", "min.", "resp."]


def clean(s):
    for pat, rep in INLINE:
        s = re.sub(pat, rep, s)
    return s.strip()


def split_sentences(text):
    t = text
    for a in sorted(ABBR, key=len, reverse=True):
        t = t.replace(a, a.replace(".", "\x00").replace(" ", "\x01"))
    t = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), t)            # 3.5
    if LANG == "de":
        t = re.sub(r"(?<![\w\x00])(\d{1,2})\.(?=\s)", lambda m: m.group(1) + "\x00", t)  # 3. Quartal
    t = re.sub(r"([.!?][\"”“')]?)\s+(?=[\"'„“(\[]?[A-ZÄÖÜ0-9])", lambda m: m.group(1) + "\x02", t)
    return [p.replace("\x00", ".").replace("\x01", " ").strip() for p in t.split("\x02") if p.strip()]


def items(kind, text, indent=0):
    """One item per sentence; a multi-sentence bullet keeps its full length on the first piece."""
    out = [{"kind": kind, "text": s, "indent": indent, "words": tokens(s), "new": [], "flags": []}
           for s in split_sentences(text)]
    for it in out[1:]:
        it["kind"] = "cont"
    if out:
        out[0]["blen"] = len(tokens(text))
    return out


def parse(text):
    """Split markdown into units (headings or ----separated slides) of sentence-like items."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":                        # YAML frontmatter
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                if any(re.match(r"^\w[\w-]*:", ln) for ln in lines[1:i]):
                    lines = lines[i + 1:]
                break
    units, para, fence = [{"title": None, "items": []}], [], False

    def flush():
        if para:
            units[-1]["items"] += items("sent", " ".join(para))
            para.clear()

    for raw in lines:
        if FENCE.match(raw):
            fence = not fence
            continue
        if fence or raw.lstrip().startswith("<!--"):
            continue
        line = raw.rstrip()
        if HR.match(line):
            flush()
            if units[-1]["title"] is not None or units[-1]["items"]:
                units.append({"title": None, "items": []})
        elif HEADING.match(line):
            flush()
            title = clean(HEADING.match(line).group(2))
            if units[-1]["title"] is not None or units[-1]["items"]:
                units.append({"title": None, "items": []})
            units[-1]["title"] = title
            units[-1]["items"] += items("title", title)
        elif BULLET.match(line):
            flush()
            m = BULLET.match(line)
            units[-1]["items"] += items("bullet", clean(m.group(2)), len(m.group(1)))
        elif line.strip().startswith("|"):
            flush()
            cells = [clean(c) for c in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) or not c for c in cells):
                units[-1]["items"] += [it for c in cells for it in items("cell", c)]
        elif not line.strip():
            flush()
        else:
            para.append(clean(line))
    flush()
    units = [u for u in units if u["title"] is not None or u["items"]]
    for ui, u in enumerate(units, 1):                              # locations: u2 title, u2 s1, u2 s2 ...
        n = 0
        for it in u["items"]:
            n += it["kind"] != "title"
            it["loc"] = f"u{ui} title" if it["kind"] == "title" else f"u{ui} s{n}"
    return units


# ---------------------------------------------------------------- terms
def tokens(s):
    return [t.strip(".,'’-") for t in re.findall(r"[\w'’\-.,]*\w", s)]


UNIT_RE = re.compile(r"(?<![\w.])(?:[€$£]\s?\d[\d.,]*\s?(?:k|m|bn|mio|mrd)?|\d[\d.,]*\s?(?:%|ms|sek|std|gb|mb|tb"
                     r"|kb|€|\$|£|k|bn|mio\.?|mrd\.?|x|pp|fte|rps|qps|px|kg|km|m²|°c|h|s|m))(?!\w)", re.I)
PLAIN_UNIT = re.compile(r"[€$£%]|\d\s?(?:k|bn|mio|mrd|h|std|min|s|sek)\.?$", re.I)
ACRO = re.compile(r"^[A-ZÄÖÜ]{2,6}s?$")
CAMEL = re.compile(r"^(?:[a-z]+[A-Z]|[A-Z][a-z]+[A-Z])\w*$")
KNOWN_ACRO = set("OK US EU UK USA IT AI KI CEO CFO CTO COO CPO CIO PDF URL HR PR FAQ GmbH AG SE B2B B2C IPO ROI KPI "
                 "SaaS ID TV PC ERP CRM GDPR DSGVO SLA EBIT EBITDA".split())
SUFFIXES = {"en": ["'s", "s", "es", "ed", "d", "ing", "ly", "er", "est", "n't"],
            "de": ["s", "n", "en", "e", "er", "es", "em", "st", "t", "te", "ten", "end", "ende", "enden", "ere",
                   "eren", "ste", "sten"]}
DEF_AFTER = re.compile(r"^\w{0,2}\s*(?:\(|=|:|,?\s*(?:is|are|means|refers to|i\.e\.|that is|heißt|bedeutet|ist|sind"
                       r"|also|d\. ?h\.)\b)", re.I)


def stem_in(w, common):
    if w in common:
        return True
    for suf in SUFFIXES[LANG]:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            base = w[: -len(suf)]
            if base in common or base + "e" in common or (base[-1] == base[-2] and base[:-1] in common):
                return True
    return False


def familiar(w, common):
    """Is the lowercase word on the common list, allowing inflection and (DE) compounds of known parts?"""
    if not common:
        return False
    w = w.replace("ß", "ss")                                       # wordfreq stores ß as ss
    if "-" in w:
        return all(familiar(p, common) for p in w.split("-") if p)
    if stem_in(w.replace("’", "'"), common):
        return True
    if LANG == "de" and len(w) >= 8:
        for i in range(4, len(w) - 3):
            head, tail = w[:i], w[i:]
            if (head in common or head.rstrip("s") in common or head.rstrip("n") in common) and stem_in(tail, common):
                return True
    return False


ALWAYS_KNOWN = {a.rstrip(".").lower() for a in ABBR} | {"heißt", "heisst", "bedeutet", "bzw", "ggf", "usw", "vs"}


def term_kind(tok, pos, common):
    """Kind of unfamiliar term, or None when the reader can be assumed to know it."""
    lw = tok.lower()
    if len(tok) < 2 or "." in tok or lw in ALWAYS_KNOWN:
        return None
    if re.search(r"\d", tok):
        return "number" if re.search(r"[A-Za-z]", tok) and not re.fullmatch(r"[QH]\d", tok) else None
    if ACRO.match(tok) and (tok[:-1] if tok.endswith("s") else tok) not in KNOWN_ACRO:
        return "acronym"
    if CAMEL.match(tok):
        return "camel"
    if not common:
        return "long" if len(lw) >= (13 if LANG == "en" else 16) or "-" in tok else None
    if LANG == "de" and len(lw) >= 20 and lw not in common:      # Bandwurm even when the parts are known
        return "long"
    if familiar(lw, common):
        return None
    if "-" in tok:
        return "compound"
    if LANG == "de" and len(lw) >= 16:
        return "long"
    if LANG == "en" and pos > 0 and tok[0].isupper() and tok[1:].islower():
        return "name"
    return "uncommon"


def defined_near(sent, surface):
    for m in re.finditer(re.escape(surface), sent):
        if DEF_AFTER.match(sent[m.end():]) or sent[: m.start()].rstrip().endswith(("(", "„", '"')):
            return True
    return False


def scan_terms(units, common, full_text):
    terms = {}

    def add(key, surface, kind, ui, loc, sent):
        if key not in terms:
            terms[key] = {"term": surface, "kind": kind, "first": loc, "unit": ui, "uses": 0,
                          "defined": defined_near(sent, surface)}
            if kind == "acronym":
                terms[key]["defined"] |= bool(re.search(r"\(" + re.escape(surface) + r"\)|" + re.escape(surface)
                                                        + r"\s*(?:\(|=|steht für|stands for)", full_text))
            is_new = True
        else:
            is_new = False
        terms[key]["uses"] += 1
        return key if is_new else None

    for ui, u in enumerate(units, 1):
        for it in u["items"]:
            text = it["text"]
            new = [add(re.sub(r"\s+", " ", m.group(0)).lower(), m.group(0).strip(), "number", ui, it["loc"], text)
                   for m in UNIT_RE.finditer(text) if not PLAIN_UNIT.search(m.group(0))]   # €, %, hours are reader's units
            for pos, tok in enumerate(tokens(UNIT_RE.sub(" ", text))):
                kind = term_kind(tok, pos, common)
                if kind:
                    new.append(add(tok.lower(), tok, kind, ui, it["loc"], text))
            it["new"] = [terms[k]["term"] for k in new if k]
    return terms


# ------------------------------------------------------------ sentences
NOM_EN = re.compile(r"\b(?:the|a|an|this|our|their|its)\s+(\w+(?:tion|ment|sion|ance|ence|ysis|ality))\s+of\b", re.I)
LIGHT_EN = re.compile(r"\b(?:make|makes|made|making|give|gives|gave|giving|have|has|had|having|take|takes|took|taking"
                      r"|reach|reaches|reached|achieve|achieves|achieved|perform|performs|performed|conduct|conducts"
                      r"|conducted|provide|provides|provided|do|does|did)\s+(?:a|an|the|our|their)?\s*"
                      r"(\w+(?:tion|ment|sion|ance|ence|ysis)|review|use|attempt|effort)\b", re.I)
# Ordinary words that end like nominalizations but are not the problem.
NOM_STOP = set("nation station moment motion mention equipment government department environment information question "
               "element document segment comment instance distance balance mission session version vision zeitung wohnung "
               "meinung rechnung ordnung bedingung abteilung lösung erfahrung bedeutung regierung richtung sitzung leitung "
               "zahlung gesellschaft wirtschaft wissenschaft landschaft freiheit gesundheit sicherheit wahrheit einheit "
               "mehrheit möglichkeit qualität universität realität identität ergebnis verhältnis kenntnis verständnis".split())
NOM_DE = re.compile(r"\b(\w{3,}(?:ung|heit|keit|ität|nis|schaft|ierung)(?:en|s|e|er)?)\b", re.I)
# Funktionsverbgefüge: noun + verb stem anywhere in the sentence.
FVG = [("Verfügung", "stell|steh"), ("Entscheidung", "treff|getroffen"), ("Betracht", "zieh|gezogen"),
       ("Einsatz", "komm|bring|gebracht"), ("Anspruch", "nehm|genommen"), ("Anwendung", "komm|find|gefunden"),
       ("Angriff", "nehm|genommen"), ("Abschluss", "bring|gebracht"), ("Kenntnis", "nehm|genommen"),
       ("Erwägung", "zieh|gezogen"), ("Berücksichtigung", "find|gefunden"), ("Umsetzung", "bring|gebracht|komm"),
       ("Prüfung", "vornehm|vorgenommen|unterz"), ("Bewertung", "vornehm|vorgenommen"), ("Verwendung", "find|gefunden"),
       ("Frage", "stell|gestellt"), ("Durchführung", "bring|gebracht|gelang"), ("Auswahl", "treff|getroffen"),
       ("Maßnahmen", "ergreif|ergriffen"), ("Stellung", "nehm|genommen|bezieh|bezogen"), ("Rechnung", "trag|getragen")]
IRREG = ("done made built sent set put held kept left lost met paid said seen shown sold taken told thought written given "
         "known run cut read found brought bought caught taught chosen driven drawn hit led won begun broken spoken "
         "understood split spent meant dealt felt hidden forgotten grown thrown struck stuck laid").split()
PASS_EN = re.compile(r"\b(?:is|are|was|were|be|been|being|get|gets|got|gotten)\s+(?:\w+ly\s+)?(\w{3,}ed|"
                     + "|".join(IRREG) + r")\b", re.I)
PASS_STOP = set("based called named located supposed interested concerned used excited pleased need indeed speed "
                "feed exceed proceed succeed breed greed seed hundred shed sacred".split())
PASS_DE = re.compile(r"\b(?:wird|werden|wurde|wurden|worden|wirst|werde|werdet)\b", re.I)
PART_DE = re.compile(r"\b((?:\w*(?:ab|an|auf|aus|ein|um|vor|zu|durch|über|unter|nach|weg|fest|frei|bereit))?ge\w{3,}"
                     r"(?:t|en)|\w{3,}iert)\b", re.I)
PART_STOP = set("gesamt gesamten geschäft geschäfte geschäften gebiet gebieten gemeinde gerät geräten gewicht gehalt "
                "gestalt gedanken gesetz gesetzen gegenwart".split())
FUNC_EN = set("the a an of to in on for with and or but is are was were be been being by at as from that this these those "
              "it its we our you your they their them him her his us me my not no can will would should could may might "
              "shall has have had do does did than then so if when which who whom whose what how where why all each every "
              "another either neither whether more most into over per via also only very just out up about after before "
              "between through during while because until both any some such new one two three first last next many much "
              "own same other well here there now like within without across under among against upon since though "
              "although unless yet nor again already always never often still even ever too almost enough something "
              "anything everything nothing someone anyone everyone".split())
VAGUE = {"en": r"\b(significant(?:ly)?|many|most|several|various|numerous|substantial(?:ly)?|considerabl[ey]|a lot of"
               r"|lots of|massive(?:ly)?|huge|vast|majority|countless|plenty of|a number of|dramatically|rapidly|greatly)\b",
         "de": r"\b(deutlich|erheblich|viele[nrs]?|zahlreiche[nrs]?|mehrere[nrs]?|diverse[nrs]?|wesentlich|signifikant"
               r"|massiv|enorm|etliche|großteils|überwiegend|ein großteil|die meisten|stark|drastisch|rasant|spürbar|merklich)\b"}
COND = {"en": r"^(?:if|unless|when|whenever|while|although|though|even though|because|since|given that|in case"
              r"|as long as|once|after|before|provided that)\b",
        "de": r"^(?:wenn|falls|sofern|solange|obwohl|während|da|weil|nachdem|bevor|sobald|auch wenn|selbst wenn|insofern)\b"}
NEG = {"en": r"\b(?:not|no|never|neither|nor|none|nothing|nobody|without|cannot)\b|n't\b",
       "de": r"\b(?:nicht|kein|keine|keinen|keinem|keiner|keines|nie|niemals|niemand|nichts|ohne|weder|nirgends)\b"}


def phrase_re(phrase, prefix=False):
    body = r"\s+".join(re.escape(p) for p in phrase.split())
    return re.compile(r"(?<!\w)" + body + (r"\w*" if prefix else r"(?!\w)"), re.I)


def check_sentence(it, filler_res):
    """Attach (level, label) flags to one sentence-like item. Levels: FLAG or HINT."""
    s, words, n, low = it["text"], it["words"], len(it["words"]), it["text"].lower()
    flags = it["flags"]
    if n > 32 and it["kind"] != "title":
        flags.append(("FLAG", f"long ({n} words)"))
    elif n > 25 and it["kind"] != "title":
        flags.append(("HINT", f"long ({n} words)"))
    if len(it["new"]) >= 3:
        flags.append(("FLAG", "cone stack: " + ", ".join(it["new"])))
    elif len(it["new"]) == 2:
        flags.append(("HINT", "2 new terms: " + ", ".join(it["new"])))
    if LANG == "en":
        noms = [m.group(1) for m in list(NOM_EN.finditer(s)) + list(LIGHT_EN.finditer(s))
                if m.group(1).lower() not in NOM_STOP]
        if noms:
            flags.append(("HINT", "nominalization: " + ", ".join(noms)))
        m = PASS_EN.search(s)
        if m and m.group(1).lower() not in PASS_STOP and not re.search(r"\bby\b", low):
            flags.append(("HINT", f'passive "{m.group(0)}" (who does this?)'))
        best = []
        for chunk in re.split(r"[,;:()\"“”]", s):                 # stacks do not cross punctuation
            run = []
            for w in tokens(chunk):
                lw = w.lower()
                if lw in FUNC_EN or len(lw) < 3 or re.search(r"\d|'", lw) or lw.endswith(("ed", "ly")) or has_verb([w]):
                    run = []
                else:
                    run.append(w)
                    best = run[:] if len(run) > len(best) else best
        if len(best) >= 4:
            flags.append(("HINT", "noun stack? " + " ".join(best)))
    else:
        noms = [m.group(1) for m in NOM_DE.finditer(s)
                if m.group(1).lower() not in NOM_STOP and re.sub(r"(en|s|e|er)$", "", m.group(1).lower()) not in NOM_STOP]
        if len(noms) >= 3 or (len(noms) == 2 and n <= 12):
            flags.append(("HINT", "Nominalstil: " + ", ".join(noms)))
        for noun, verb in FVG:
            if re.search(noun, s, re.I) and re.search(r"\b(?:" + verb + r")", s, re.I):
                flags.append(("HINT", f"Funktionsverbgefüge: {noun} + {verb.split('|')[0]}-"))
        aux, part = PASS_DE.search(s), [m for m in PART_DE.finditer(s) if m.group(1).lower() not in PART_STOP]
        if aux and part and not re.search(r"\b(?:von|vom|durch|seitens)\b", low):
            flags.append(("HINT", f'Passiv ohne Akteur "{aux.group(0)} … {part[0].group(1)}" (wer?)'))
        long_words = [w for w in words if len(w) >= 20]
        if long_words:
            flags.append(("HINT", "Bandwurmwort: " + ", ".join(long_words)))
    m = re.search(VAGUE[LANG], low)
    if m and not re.search(r"\d", s):
        flags.append(("HINT", f'vague amount "{m.group(1)}" (no number)'))
    if re.match(COND[LANG], low):
        head = s.split(",")[0]
        lead = len(tokens(head))
        if lead >= 10:
            flags.append(("HINT", f"condition first ({lead} words before the main clause)"))
    negs = re.findall(NEG[LANG], low)
    if len(negs) >= 2:
        flags.append(("HINT", f"{len(negs)} negations"))
    hits = [p for p, rx in filler_res if rx.search(s)]
    if hits:
        flags.append(("HINT", "filler: " + ", ".join(hits[:4])))
    tail = re.search(r",\s+(?:with|including|plus|mit|inklusive|samt)\s+[^,]{3,60}$", s.rstrip(".!? "), re.I)
    if tail and n >= 18 and tail.start() > 0.6 * len(s):           # "…, with the source for every finding"
        flags.append(("HINT", f'trailing qualifier "{tail.group(0).strip(", ")[:40]}" (own sentence?)'))
    for rx, label in SHAPES[LANG]:                                 # generated-sounding sentence shapes
        if label.endswith("?") and it["kind"] not in ("sent", "cont"):
            continue                                               # semicolons in list steps are not antithesis
        if re.search(rx, s.strip(), re.I):
            flags.append(("FLAG" if it["kind"] == "title" else "HINT", "AI shape: " + label))
            break


# Sentence shapes that read as generated even when every word is fine (see references/voice.md).
SHAPES = {
    "en": [(r"\w,\s+not\s+(?!only\b|just\b|necessarily\b|least\b|to\b|yet\b)\w", "X, not Y"),
           (r"\bnot\s+(?:just|only|merely|simply)?\s*[^.;:]{1,50}?,?\s+but\s+(?:also\s+)?\w", "not X but Y"),
           (r"\b(?:it|this|that)(?:'s|’s| is) not\b[^.]{1,60}\.\s*(?:it|this|that)(?:'s|’s| is)\b", "it's not X, it's Y"),
           (r"^by the time\b", "by the time X, Y"),
           (r"^(?:the\s+)?(?:result|answer|catch|truth|kicker|bottom line|takeaway|twist|upshot)\s*[:?]", "colon reveal"),
           (r"^here(?:'s|’s| is)\s+(?:the|what|why|how)\b", "staged setup"),
           (r"^[^;]{3,60};\s*[^;]{3,60}$", "mirrored pair?")],
    "de": [(r"\w,\s+nicht\s+(?!nur\b|mehr\b|zuletzt\b|wahr\b|immer\b)\w", "X, nicht Y"),
           (r"\bnicht\s+(?:nur\s+)?[^.;:]{1,50},\s*sondern\b", "nicht X, sondern Y"),
           (r"^(?:das\s+)?(?:ergebnis|fazit|die antwort|der clou|der haken|die wahrheit|kurz gesagt)\s*[:?]",
            "Doppelpunkt-Enthüllung"),
           (r"^[^;]{3,60};\s*[^;]{3,60}$", "Spiegelpaar?")],
}


# ------------------------------------------------------------- units/AI
# Verb stems that mark a title as a claim (prefix match from 4 letters, exact match below).
VERBS = {"en": ("is are was were be has have had will would can could should must need cut save cost grow drop fall rise "
                "beat win lose reduce increase double halve pay deliver drive mean matter require show stop start move make "
                "take keep get give let go come run work fail break block lead buy sell ship launch own decide want expect "
                "add use put miss turn stay hold change become bring see know look wait fell grew lost won went came ran "
                "became broke led sold bought paid made took gave got kept held brought saw knew propose recommend "
                "suggest ask plan approve agree invest hire replace reach prove find test measure arrive remain").split(),
         "de": ("ist sind war wird werden wurde hat haben kann können muss müssen soll sollen will wollen brauch kost spar "
                "senk steig sink wachs wächst fäll bring mach zeig fehl bleib geh komm lieg steh gibt nutz zahl verlier "
                "gewinn entscheid start lauf läuft reich lohn halbier verdoppel reduzier erhöh dauer schaff scheiter "
                "blockier verkauf kauf bau").split()}


def has_verb(words):
    if len(words) >= 3 and words[0].lower() in ("we", "you", "they", "wir", "sie", "ihr") and words[1].islower():
        return True                                                # "We propose …", "Wir empfehlen …"
    if any(lw == v or (len(v) >= 4 and lw.startswith(v)) for lw in (w.lower() for w in words) for v in VERBS[LANG]):
        return True
    # Longer titles: a lowercase word after the first that looks inflected is probably a verb ("drifts", "läuft").
    ends = ("s", "ed") if LANG == "en" else ("t", "en", "te")
    det = {"the", "a", "an", "all", "our", "your", "their", "its", "these", "those", "key", "new", "many", "more", "most",
           "some", "die", "der", "das", "den", "dem", "des", "ein", "eine", "einen", "einem", "einer", "alle", "aller",
           "unsere", "ihre", "im", "am", "zum", "zur", "vom", "beim", "ins", "mit", "von", "für", "auf", "bei", "nach"}
    not_verbs = {"this", "his", "its", "as", "us", "thus", "plus", "across", "always", "perhaps", "towards", "sometimes",
                 "selten", "zwischen", "unten", "oben", "hinten", "vorne", "jetzt", "nicht", "bereits", "meist", "zuerst"}
    return len(words) >= 6 and any(w.islower() and w.endswith(ends) and not w.endswith(("ss", "'s"))
                                   and w not in not_verbs and words[i].lower() not in det
                                   for i, w in enumerate(words[1:]))


def check_unit(u):
    flags, title = [], u["title"]
    if title:
        tw = tokens(title)
        if len(tw) > 15:
            flags.append(f"long title ({len(tw)} words)")
        elif title.endswith("?"):
            flags.append("question title")
        elif len(tw) <= 3 or not (has_verb(tw) or re.search(r"\d", title)):
            flags.append("topic title (no claim)")
    groups, prev = [], None                                        # sibling bullets of the same indent
    for it in u["items"]:
        if it["kind"] == "cont":
            continue
        key = (it["kind"], it["indent"])
        if it["kind"] == "bullet" and key == prev:
            groups[-1].append(it["blen"])
        elif it["kind"] == "bullet":
            groups.append([it["blen"]])
        prev = key
    for g in groups:
        if len(g) >= 3 and max(g) >= 2.5 * min(g) and max(g) - min(g) >= 6:
            flags.append(f"uneven bullets ({min(g)}–{max(g)} words)")
    run = 0                                                        # "Fast. Simple. Secure." drumbeats
    for it in u["items"]:
        run = run + 1 if it["kind"] in ("sent", "cont") and len(it["words"]) <= 3 else 0
        if run == 3:
            flags.append("fragment drumbeat (3+ short fragments in a row)")
    body = [it for it in u["items"] if it["kind"] != "title" and it["words"]]
    for a, b, c in zip(body, body[1:], body[2:]):                  # "It flags… It flags… It drafts…"
        if a["words"][0].lower() == b["words"][0].lower() == c["words"][0].lower():
            flags.append(f'same opener 3× in a row: "{a["words"][0]}"')
            break
    para, note_words, in_note = [], 0, False                       # quip closers: short last line of a paragraph
    for it in body + [None]:
        if it is None or it["kind"] in ("sent", "bullet", "cell"):
            is_note = bool(para) and NOTE.match(para[0]["text"])
            if (len(para) >= 3 or (is_note and len(para) >= 2)) and len(para[-1]["words"]) <= 10 \
                    and not re.search(r"\d", para[-1]["text"]):
                para[-1]["flags"].append(("HINT", "closer? (short last line of a paragraph)"))
            para = []
            in_note = it is not None and bool(NOTE.match(it["text"]))
        if it is not None and (in_note or SOURCE.match(it["text"])):
            note_words += len(it["words"])                         # notes and source lines are not slide text
        if it is not None and it["kind"] in ("sent", "cont"):
            para.append(it)
    new = sum(len(it["new"]) for it in u["items"])
    if new > 2:
        flags.append(f"{new} new terms (budget 2)")
    u["words"] = sum(len(it["words"]) for it in u["items"] if it["kind"] != "title") - note_words
    if DECK and u["words"] > 40:
        flags.append(f"{u['words']} words on the slide (notes excluded; aim for about 40)")
    u["new"], u["flags"] = new, flags


def scan_ai(units, ai):
    hits = []
    for ui, u in enumerate(units, 1):
        for it in u["items"]:
            for phrase, level in ai:
                if phrase_re(phrase, prefix=True).search(it["text"]):
                    hits.append({"phrase": phrase, "level": level, "unit": ui})
    return hits


# -------------------------------------------------------------- summary
FUNC_OPENERS = {"the", "a", "an", "die", "der", "das", "ein", "eine", "notiz", "note", "notes"}
NOTE = re.compile(r"^(?:notiz|notes?|speaker notes?|sprechernotiz)\s*:", re.I)   # speaker notes in decks
SOURCE = re.compile(r"^(?:source|sources|quelle|quellen)\s*:", re.I)
TRIPLET = re.compile(r"\b[\w-]+(?: [\w-]+){0,2}, [\w-]+(?: [\w-]+){0,2},? (?:and|und|or|oder) [\w-]+", re.I)
DECK = False                                                       # set in main() when slides are separated by ---
TITLE_CONNECTORS = {"en": {"'X because Y'": [" because ", ", so ", ", therefore "], "'X, not Y'": [", not ", " but "],
                           "'Label: claim'": [": "]},
                    "de": {"'X, weil Y'": [", weil ", ", deshalb ", ", denn ", ", daher "],
                           "'X, nicht Y'": [", nicht ", ", sondern ", ", aber "], "'Label: Aussage'": [": "]}}


def syllables(w):
    w, n = w.lower(), len(re.findall(r"[aeiouyäöü]+", w.lower()))
    if LANG == "en" and n > 1 and w.endswith("e") and not w.endswith(("le", "ee")):
        n -= 1
    return max(1, n)


def summarize(units, terms, text):
    items = [it for u in units for it in u["items"]]
    words = [w for it in items for w in it["words"]]
    nw, ns = max(1, len(words)), max(1, sum(it["kind"] != "title" for it in items))
    letters = [w for w in words if re.search(r"[A-Za-zÄÖÜäöüß]", w)]
    syl = sum(syllables(w) for w in letters) / max(1, len(letters))
    lix = nw / ns + 100 * sum(len(w) > 6 for w in words) / nw
    read = 180 - nw / ns - 58.5 * syl if LANG == "de" else 206.835 - 1.015 * nw / ns - 84.6 * syl
    low = re.findall(r"[a-zäöüß']+", text.lower())
    buts = sum(low.count(w) for w in ("but", "however", "yet", "although", "aber", "doch", "jedoch", "allerdings", "sondern"))
    ands = low.count("and") + low.count("und")
    hard = sum(1 for it in items for lv, _ in it["flags"] if lv == "FLAG")
    soft = sum(1 for it in items for lv, _ in it["flags"] if lv == "HINT") + sum(len(u["flags"]) for u in units)
    body = sum(len(it["words"]) for it in items if it["kind"] != "title")
    lens = [len(it["words"]) for it in items if it["kind"] in ("sent", "cont") and len(it["words"]) > 3]
    mean = sum(lens) / max(1, len(lens))
    sd = (sum((n - mean) ** 2 for n in lens) / max(1, len(lens))) ** 0.5
    patterns = []
    if len(lens) >= 8 and sd < (5 if DECK else 6):                 # slides are short by design, but not uniform
        patterns.append(f"uniform sentence length (sd {sd:.1f} words; mix short sentences with longer ones)")
    triplets = len(TRIPLET.findall(text))
    if triplets >= 4 and triplets >= 0.006 * len(words):
        patterns.append(f"{triplets} lists of exactly three ('a, b and c'); use the number of items the facts have")
    starts = Counter(it["words"][0].lower() for it in items if it["words"])
    top, n = starts.most_common(1)[0] if starts else ("", 0)
    if n >= 4 and n >= 0.15 * sum(starts.values()) and top not in FUNC_OPENERS:
        patterns.append(f'"{top}" opens {n} of {sum(starts.values())} sentences and titles')
    titles = [u["title"].lower() for u in units if u["title"]]
    for name, conns in TITLE_CONNECTORS[LANG].items():
        k = sum(any(c in t for c in conns) for t in titles)
        if k >= 2:
            patterns.append(f"{k} titles share the {name} shape")
    firsts = Counter(t.split()[0] for t in titles if t.split())
    if firsts and firsts.most_common(1)[0][1] >= 3:
        patterns.append(f'{firsts.most_common(1)[0][1]} titles start with "{firsts.most_common(1)[0][0]}"')
    return {"lang": LANG, "words": len(words), "body_words": body, "units": len(units), "sentences": len(items),
            "terms": len(terms), "sentence_sd": round(sd, 1), "patterns": patterns,
            "load": round(100 * len(terms) / nw, 1), "flags_per_100": round(100 * (hard + soft) / nw, 1),
            "hard": hard, "soft": soft, "lix": round(lix), "readability": round(read),
            "narrative": {"but": buts, "and": ands, "index": round(buts / max(1, ands), 2)}}


# --------------------------------------------------------------- output
def cut(s, n=110):
    return s if len(s) <= n else s[: n - 1] + "…"


def report(units, terms, ai_hits, summ, heuristic):
    out = [f"## Titles (storyline) · {len(units)} units" + (" · heuristic mode (no common list)" if heuristic else "")]
    for ui, u in enumerate(units, 1):
        flag = ("  ← " + "; ".join(u["flags"])) if u["flags"] else ""
        out.append(f"u{ui} ({u['words']} w) {u['title'] or '(no title)'}{flag}")
    out += ["", f"## Terms (concept chart) · {len(terms)} unfamiliar terms · load {summ['load']} per 100 words"]
    rows = sorted(terms.values(), key=lambda t: (t["unit"], t["first"]))
    out.append(f"{'term':<28}{'first':<9}{'uses':<6}{'defined':<9}kind")
    for t in rows[:40]:
        out.append(f"{cut(t['term'], 26):<28}{t['first']:<9}{t['uses']:<6}{'yes' if t['defined'] else 'no':<9}{t['kind']}")
    if len(rows) > 40:
        out.append(f"… {len(rows) - 40} more (use --json)")
    out.append("new terms per unit: " + " · ".join(f"u{i} {u['new']}{'!' if u['new'] > 2 else ''}" for i, u in enumerate(units, 1)))
    undefined = [t["term"] for t in rows if t["kind"] == "acronym" and not t["defined"]]
    if undefined:
        out.append("undefined acronyms: " + ", ".join(undefined))
    flagged = [it for u in units for it in u["items"] if it["flags"]]
    flagged.sort(key=lambda it: (-sum(lv == "FLAG" for lv, _ in it["flags"]), -len(it["flags"]), -len(it["words"])))
    out += ["", f"## Sentences · {len(flagged)} of {summ['sentences']} flagged · worst {min(15, len(flagged))}"]
    for it in flagged[:15]:
        marks = " · ".join(("!! " if lv == "FLAG" else "! ") + label for lv, label in it["flags"])
        out += [f"{it['loc']} · {len(it['words'])} w · {marks}", f"   {cut(it['text'])}"]
    cuts = Counter(h["phrase"] for h in ai_hits if h["level"] == "CUT")
    highs = Counter((h["unit"], h["phrase"]) for h in ai_hits if h["level"] == "HIGHLIGHT")
    out += ["", f"## AI filler · {sum(cuts.values())} CUT · {sum(highs.values())} HIGHLIGHT"]
    for phrase, n in cuts.most_common():
        where = sorted({h["unit"] for h in ai_hits if h["phrase"] == phrase})
        out.append(f"CUT  {phrase} ×{n}  (u{', u'.join(map(str, where))})")
    per_unit = Counter(u for u, _ in highs.elements())
    for ui in sorted(u for u, n in per_unit.items() if n >= 2):
        out.append(f"HIGHLIGHT cluster u{ui}: " + ", ".join(sorted({p for u, p in highs if u == ui})))
    if sum(highs.values()) and not any(n >= 2 for n in per_unit.values()):
        out.append("highlight words spread thin, no clusters")
    shapes = [(it["loc"], label[10:]) for u in units for it in u["items"] for _, label in it["flags"]
              if label.startswith("AI shape: ")]
    if shapes:
        out.append(f"AI shapes · {len(shapes)}: " + " · ".join(f"{loc} {label}" for loc, label in shapes[:12]))
    for p in summ["patterns"]:
        out.append(f"AI pattern: {p}")
    s = summ
    out += ["", f"## Summary · {s['lang']} · {s['words']} words ({s['body_words']} body) · {s['units']} units · "
                f"{s['sentences']} sentences",
            f"load: {s['load']} new terms / 100 words · flags: {s['flags_per_100']} / 100 words "
            f"({s['hard']} hard, {s['soft']} soft) · compare drafts, no target",
            f"LIX {s['lix']} · {'Flesch-Amstad' if s['lang'] == 'de' else 'Flesch'} {s['readability']} · "
            f"narrative index {s['narrative']['but']} but : {s['narrative']['and']} and ({s['narrative']['index']})"]
    return "\n".join(out)


def main():
    global LANG, DECK
    ap = argparse.ArgumentParser(description="Clarity scan: titles, terms, sentences, AI filler, load.")
    ap.add_argument("file", nargs="?", help="markdown or text file (default: stdin)")
    ap.add_argument("--lang", choices=["en", "de"], help="default: auto-detect by function words")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--known", default="", help="comma-separated terms this reader knows (product names, their jargon)")
    args = ap.parse_args()
    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    LANG = args.lang or detect_lang(text)
    DECK = len(re.findall(r"^---\s*$", text, re.M)) >= 3
    common = set(w.strip().lower() for w in read_list(f"common_{LANG}.txt"))
    known = args.known.split(",") + read_list(f"business_{LANG}.txt")   # the reader's own vocabulary is free
    known_words = {w.lower() for term in known for w in re.split(r"[\s-]+", term.strip()) if w}
    ALWAYS_KNOWN.update(known_words)
    if common:
        common |= known_words                                      # so inflected forms match too
    ai = [(ln.split("\t")[0].strip().lower(), (ln.split("\t") + ["HIGHLIGHT"])[1].strip().upper())
          for ln in read_list(f"ai_{LANG}.txt")]
    filler_res = [(p.lower(), phrase_re(p)) for p in read_list(f"filler_{LANG}.txt")]
    units = parse(text)
    terms = scan_terms(units, common, text)
    for u in units:
        for it in u["items"]:
            check_sentence(it, filler_res)
        check_unit(u)
    ai_hits = scan_ai(units, ai)
    summ = summarize(units, terms, text)
    if args.json:
        print(json.dumps({"summary": summ, "units": [{k: u[k] for k in ("title", "words", "new", "flags")} for u in units],
                          "terms": list(terms.values()), "ai": ai_hits,
                          "sentences": [{"loc": it["loc"], "text": it["text"], "words": len(it["words"]), "new": it["new"],
                                         "flags": it["flags"]} for u in units for it in u["items"] if it["flags"]]},
                         ensure_ascii=False, indent=1))
    else:
        print(report(units, terms, ai_hits, summ, heuristic=not common))


if __name__ == "__main__":
    main()
