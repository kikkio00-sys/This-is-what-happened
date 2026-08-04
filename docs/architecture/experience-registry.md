# Experience Registry

The Experience Registry is the typed source for LifeCove destinations. Navigation and experience lists should read from `src/config/experiences.ts` rather than hard-coding separate destination lists.

Fields: `id`, `name`, `shortDescription`, `route`, `status`, `environment`, `chief`, `visibility`, and `navigationOrder`.

Future experiences are added by registering one plain typed object and then creating the matching route. Do not introduce plugin loading or dynamic packages for V0.1.
