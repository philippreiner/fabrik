# Verification

Green lint, typecheck, and tests establish a baseline; they do not prove behavior is correct. Write tests that do not change when the implementation changes: a test that needs editing for every refactor verified the wrong thing.

- Test database behavior in an integration suite with real migrations and the owning module's transitions, faking only external boundaries. `docs/development/quality-loop.md` defines their isolation. Cover the relevant constraint, denied precondition, repeat operation, or partial failure.
- A race test runs the competing writes on separate connections and asserts the one outcome; it complements, never replaces, the constraint or lock that guarantees it.
- Check that assertions prove the caller's required outcome through returned values, persisted rows, responses, events, or rendered output. A mock agreeing with the implementation does not establish correctness.
- For added or touched tests, name a plausible broken implementation that would fail the test and a behavior-preserving refactor that should pass unchanged. Flag assertions that merely mirror branches, mocks, constants, or private call order. Before removing a test, identify its unique failure coverage and where that coverage belongs; keep isolated tests when they catch meaningful failures broader tests cannot reliably exercise.
- Cover the most important bad path, permission boundary, malformed input, and affected concurrency or idempotency risk. Test revoked membership, removed assignment, and foreign-tenant IDs where access changes.
- A speed claim needs a measurement before and after. Locally, read the server timing of the changed calls. On the deployed site, send repeated requests to a runtime-only and a one-query health endpoint to separate cold starts, runtime, and database time, and confirm the deployed build is the commit you measured. Name an unmeasured cause as inference.
- Runtime, binding, or bundle changes need a build or check in the target runtime. Node-only mocks cannot establish deployment compatibility or browser isolation.
- Verify changed retry, claim, and pagination behavior on its important failure path. Verify invalidation, telemetry, and AI tracing when the observable outcome depends on them.
- Update a test when the DOM shape changes on purpose. Do not preserve markup to keep a query alive.
- If local configuration hides UI needed for review, enable the feature using an existing local mechanism, inspect it, and restore temporary changes. For flag changes, check both states. If setup is unavailable, report the visual check as blocked; component tests do not replace it.
- Open the browser only for changed behavior, such as saving, navigation, or permissions, that reading the code cannot settle.
- E2E runs only when the user asks; for a larger browser-flow change, name in the pull request whether a spec should cover it.

## Lint Warnings And Test Seams

- Diagnose a lint warning before restructuring production code. Never widen a production type, drop validation, or add a test-only override to authorization, permission, or persistence code so a fake fits.
- Do not add module mocks of our own packages in new tests; prefer the seams below. Framework runtime that cannot execute under the test runner may be mocked.
- Choose the fake by what the test depends on:
  - A decision (branching, parsing, mapping, classification): test it as a pure function. Extract it when it sits inline; that is a move, not a rewrite.
  - A collaborator the code already accepts as a parameter or deps object: pass a fake. Do not add a collaborator parameter to thin glue only so a test can run.
  - Database rules, permissions, tenant isolation, idempotency, settlement: prove it in an integration suite against the real database, not against a mocked repository.
  - An external provider (email, a model, a webhook sender): fake it at its boundary, through an injected client or model, or `vi.stubGlobal("fetch")`. Never module-mock our own client wrapper.
  - Environment and globals: `vi.stubEnv`, `vi.stubGlobal`, and `vi.spyOn` on a real object are fine. They replace a value, not a module.
- Never make a test pass by weakening its assertions.
- Never let a refactor emerge from fixing failing tests one by one. Tests steered by the work they check are not checks.
- A comparison test proves nothing unless its output is sensitive to the behavior under test. Saturated values, all-zero outputs, and round-trips through lossy identity all pass for broken code.
- Delete a test whose assertions restate its mocks, such as glue that authorizes, calls the domain module, and revalidates. Name the integration case or Playwright spec that owns the behavior, or record the journey as an E2E candidate.
