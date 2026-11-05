# TypeScript

Use the type checker to rule out impossible states, mixed-up values, and unhandled variants at compile time. [contracts-and-permissions.md](contracts-and-permissions.md) owns boundary parsing, Zod-derived types, and `satisfies`.

- **Make illegal states unrepresentable.** Model variants as a discriminated union on a `kind` or status literal, not a bag of optional fields. `{ completed: boolean; completedAt?: Date }` admits a completed item without a date; derive the flag from `completedAt !== null` or use `{ kind: "open" } | { kind: "done"; at: Date }`. If you can write a comment explaining when a field combination is valid, split the type.
- **Construct, do not restrict.** Build the shape that cannot hold the illegal value: `[T, ...T[]]` for non-empty, start plus duration for a range. Strengthen a type only where the loose one forces `!`, a cast, or a "should never happen" throw; otherwise keep the plain type.
- **Exhaust variants.** In a switch over a union, end with `const _exhaustive: never = value;` so the compiler names the next place to handle a new variant.
- **Do not lie to the compiler.** `unknown` over `any` for external data. A cast is acceptable only after validation. A type guard (`isX`, `hasX`) must check what it claims; a lying guard is worse than `as`.
- **Narrow in this order:** discriminant switch, `in`, `typeof` or `instanceof`, a verified guard, and `as` last.
- **Derive, do not redeclare.** Reach for `Pick`, `Omit`, `ReturnType`, `Awaited`, `typeof`, or the ORM or schema source before writing a parallel interface.
- **Distinct IDs.** When a signature takes two IDs of the same primitive type that mean different things (`userId` and `actorUserId`), name them apart. Add a brand only after a real mix-up or where a bare string crosses many layers; one brand used in one place is noise.
- **Object arguments** for functions with more than two parameters or any two of the same type, so call sites read without the signature.
