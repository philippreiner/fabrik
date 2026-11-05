# UI and server

Check framework behavior against its current docs. `docs/architecture.md` names
the framework, the request-path budget, and the canonical helpers.

## Server Boundary

- Know which code runs on both server and client (in many frameworks, loaders and route guards). Privileged work belongs inside server-function handlers or server routes, including reads used by loaders. A server-only helper is not an endpoint; a folder name or `async` keyword does not establish a server boundary.
- Every server function is callable independently of its page. Validate input and enforce the relevant session, account state, tenant, and capability there. Public auth functions and operational routes use their own explicit access contract.
- Resolve the actor from the session. Treat posted IDs, route params, slugs, and search values as untrusted selectors; verify current access to the selected tenant and object. Parent route guards do not secure child loaders or mutations.
- Keep loaders and GET handlers free of product mutations: navigation, preloading, and retries may repeat them. Use POST for mutations and preserve the framework's CSRF boundary.
- Review browser-reachable imports and serialized loader data for secrets, server package roots, and unnecessary private fields. Types and file placement alone do not prove bundle isolation.
- Create router and user-specific request context per request. Authentication, locale, and tenant data must not leak through module caches or SSR state.
- Regenerate generated output (route trees, types) through its tooling rather than editing it.

## Navigation, Loaders, And Revalidation

- Validate URL search state and include relevant values in loader dependencies. Use typed navigation. Preserve redirects and not-found control flow through error mapping.
- Successful writes revalidate through one owner; do not compensate with manual refetch loops. Verify same-route edits, tenant switches, and auth changes cannot leave stale permissions or content visible.
- A server call admits once, then runs the screen's independent reads in parallel within the step budget. A growing step count is a finding.
- A loader makes one server call. Data shared by sibling tabs loads in their parent route. Picker, menu, and dialog options load when the control opens; a screen read that grows with tenant data for a control the user may not open is a finding.
- The request path awaits the database, storage, and the provider call it exists for. A flag, analytics, or telemetry call on it is a finding even behind a timeout: the timeout bounds the stall, not how often it happens.
- Route files import only light modules at top level; heavy libraries load lazily.
- Check direct SSR entry and client navigation when the changed boundary can behave differently. Hydration must agree on locale, dates, theme, and initial data.

## State And Effects

Keep these states separate:

- **server state**: database, API, and workflow truth, delivered through loaders
- **URL state**: navigation, filters, tabs, sort, and pagination
- **local UI state**: sheet open, draft input, and step index

- Do not store derived data in state or mirror props or loader data into state.
- Use effects only to synchronize with an external system. Use props, keyed remounts, URL state, optimistic updates, or event handlers for application state.
- Replace booleans that describe one mode with a discriminated state.
- Remove a state setter when a downstream expression can always override its value.
- Reuse the form lifecycle and feedback owners. Preserve submitted values on failure, prevent accidental repeat submission, and preserve keyboard access and focus recovery.
- Render user-facing dates, times, and numbers through the product's format helpers with the user's locale and time zone.

## Errors And Telemetry

- Define typed errors at domain and transport boundaries and classify them by recovery: retry transient failures within bounds; invalid configuration or denied access needs a remedy before retry.
- Fail loudly on missing rows, invalid transitions, and impossible states. Do not hide contract failures behind fallbacks or broad catches.
- Unexpected errors reach operational telemetry even when mapped to a generic user message; `console.error` is not telemetry. Identify the failed step and tenant, redact sensitive data, and say whether retry is safe.
- Run independent work in parallel when it keeps orchestration clear.

## Public Ingress And Providers

- Authenticate webhooks and inbound email, and deduplicate deliveries before durable effects. Bound declared and streamed request bytes before full buffering or expensive work.
- For fetched user or provider URLs, allowlist the scheme and destination, handle redirects explicitly, and bound streamed response bytes.
- Bind opaque cursors to their tenant, resource, and operation. Paginated filtering must fill the requested page without unbounded enumeration; use one stable unique order for sorting and continuation.
- Provider calls inside workflows and retry loops need an abort timeout. Keep provider policy, error redaction, and retry interpretation in canonical adapters.
