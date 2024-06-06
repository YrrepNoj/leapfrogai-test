# Changelog

## [0.8.0](https://github.com/YrrepNoj/leapfrogai-test/compare/v0.7.2...v0.8.0) (2024-06-06)


### Features

* Add ability edit delete assistants within the UI ([#510](https://github.com/YrrepNoj/leapfrogai-test/issues/510)) ([e8408b7](https://github.com/YrrepNoj/leapfrogai-test/commit/e8408b75468902861a41c11060ae4d0b138f24ad))
* add chat and completion pbs ([5e8dd4b](https://github.com/YrrepNoj/leapfrogai-test/commit/5e8dd4b83b17e920d8a8d1e15f88618dd8b86d79))
* add chat proto and mpt model impl ([f537f26](https://github.com/YrrepNoj/leapfrogai-test/commit/f537f26366cb05698f75fcf2cc02552208205115))
* Add supabase deployment package ([#380](https://github.com/YrrepNoj/leapfrogai-test/issues/380)) ([8982bc0](https://github.com/YrrepNoj/leapfrogai-test/commit/8982bc08e7e2dac496409a38e3f53f7757c3bdbf))
* add working embedding endpoint for all-minilm-l6-v2 ([a03187a](https://github.com/YrrepNoj/leapfrogai-test/commit/a03187a47905e1eec2af8f53fdba07761b6a4586))
* add working HF chat model for mpt-7b-chat ([0d5d818](https://github.com/YrrepNoj/leapfrogai-test/commit/0d5d818f7e730dc5941938351946adc8ce0f15d0))
* **API:** Add authentication ([#533](https://github.com/YrrepNoj/leapfrogai-test/issues/533)) ([a634a59](https://github.com/YrrepNoj/leapfrogai-test/commit/a634a59d011fbbd2a355458e3bad711af16cb5df))
* **api:** assistants endpoint ([#424](https://github.com/YrrepNoj/leapfrogai-test/issues/424)) ([0c483a1](https://github.com/YrrepNoj/leapfrogai-test/commit/0c483a1fd1848836bb1d964d0f1c831c26957ea6))
* factor chat proto into separate services for steam and non-stream ([1bbabb9](https://github.com/YrrepNoj/leapfrogai-test/commit/1bbabb937fc2199050b955f2a4cfde1107059681))
* factor the api code into files for each endpoint ([536c9eb](https://github.com/YrrepNoj/leapfrogai-test/commit/536c9eb7bd021b90696afe3cc12401f6ae7fd105))
* files endpoints ([#467](https://github.com/YrrepNoj/leapfrogai-test/issues/467)) ([c269eee](https://github.com/YrrepNoj/leapfrogai-test/commit/c269eee174124949b103240110bd1eae5177d301))
* finish renaming completion + generation protos ([9746419](https://github.com/YrrepNoj/leapfrogai-test/commit/974641932cf3861663ad868a5f7e64f803eab9b2))
* fix gitignore to exclude local model files ([2127ed8](https://github.com/YrrepNoj/leapfrogai-test/commit/2127ed82f4fd6de1501aba21b0c648d1091bb35a))
* LLM Backend ADR and ADR Template ([#262](https://github.com/YrrepNoj/leapfrogai-test/issues/262)) ([ff278c2](https://github.com/YrrepNoj/leapfrogai-test/commit/ff278c21b081785a6b82e3104a768a70b2b778de))
* remove pytorch and nvidia dependencies that are already included in our base image ([6a9a4d4](https://github.com/YrrepNoj/leapfrogai-test/commit/6a9a4d4074354023684e5465229f03dc776597b1))
* rename chat.proto's CompletionChoice to ChatCompletionChoice ([50a62b5](https://github.com/YrrepNoj/leapfrogai-test/commit/50a62b5e34795e2ee01c37248607bc3b92654cd6))
* renamed generate endpoint to completion ([b320868](https://github.com/YrrepNoj/leapfrogai-test/commit/b32086888bf1ee83f24f316f2bc3c5ae89f6ae6f))
* sidenav redesign with import and export ([#398](https://github.com/YrrepNoj/leapfrogai-test/issues/398)) ([368e4e9](https://github.com/YrrepNoj/leapfrogai-test/commit/368e4e9b152a126a02473dbff46875da94c58d3a))
* textarea instead of text input ([#435](https://github.com/YrrepNoj/leapfrogai-test/issues/435)) ([47a0fba](https://github.com/YrrepNoj/leapfrogai-test/commit/47a0fba2196fd3ea67d0190401a9247f1bad5803))
* ui assistants management ([#469](https://github.com/YrrepNoj/leapfrogai-test/issues/469)) ([28ba7ed](https://github.com/YrrepNoj/leapfrogai-test/commit/28ba7edd1cdd22eda99b50a3fe08f987cc53e020))
* **ui:** 531 file management ([#558](https://github.com/YrrepNoj/leapfrogai-test/issues/558)) ([884761b](https://github.com/YrrepNoj/leapfrogai-test/commit/884761b06dde49bb701cc25678fefd03248cd102))
* **ui:** Assistant Avatars ([#494](https://github.com/YrrepNoj/leapfrogai-test/issues/494)) ([b4d9cfc](https://github.com/YrrepNoj/leapfrogai-test/commit/b4d9cfc0b2d7b6d89f0efc0d6d76438fd2f9d92e))
* **ui:** dates ([#404](https://github.com/YrrepNoj/leapfrogai-test/issues/404)) ([7efcebf](https://github.com/YrrepNoj/leapfrogai-test/commit/7efcebfceac3a3f9670005ebb9ba6ba6e977d94d))
* **ui:** Utilize OpenAI for backend ([#553](https://github.com/YrrepNoj/leapfrogai-test/issues/553)) ([5371956](https://github.com/YrrepNoj/leapfrogai-test/commit/5371956867d6a98196e22ec24574f885c25bce80))
* update tests to not use the response.text field ([ba626dd](https://github.com/YrrepNoj/leapfrogai-test/commit/ba626ddcc11e6504981fca2b2a11b63d339ea57f))
* updated chat completion proto ([0e7a46c](https://github.com/YrrepNoj/leapfrogai-test/commit/0e7a46cce4e94736d6cfc0ec936c7001ea39b299))
* working container for mpt-chat model ([34130c5](https://github.com/YrrepNoj/leapfrogai-test/commit/34130c5cd1d590720307bd36bdee4baf66d3f8e5))
* working huggingchat api compatibility ([0fbfd17](https://github.com/YrrepNoj/leapfrogai-test/commit/0fbfd171c3d186c6dea46951e51936ff5e38b77d))
* working implementation of streaming + non-streaming chat endpoint ([8c53d88](https://github.com/YrrepNoj/leapfrogai-test/commit/8c53d88e4722d771578cf2c45db0c23034e3dbd8))


### Bug Fixes

* allow release-please to update pyrpoject.toml files ([#509](https://github.com/YrrepNoj/leapfrogai-test/issues/509)) ([3e1f0a6](https://github.com/YrrepNoj/leapfrogai-test/commit/3e1f0a6c3a749e868caabf31035ddbbe6831bb1c))
* cleanup for pr ([8b3fd50](https://github.com/YrrepNoj/leapfrogai-test/commit/8b3fd5052864316c5aaefc75f7eca77378d03b37))
* correct typos in e2e workflow path triggers ([#376](https://github.com/YrrepNoj/leapfrogai-test/issues/376)) ([ab29743](https://github.com/YrrepNoj/leapfrogai-test/commit/ab297431d2d5acb26b4d6f5c3e231e904b0b7e76))
* fix release workflow from calling the wrong make target ([#383](https://github.com/YrrepNoj/leapfrogai-test/issues/383)) ([7b4dc7c](https://github.com/YrrepNoj/leapfrogai-test/commit/7b4dc7c658afc7ca7118dacb781d2451d82d6cab))
* input resize bug ([#472](https://github.com/YrrepNoj/leapfrogai-test/issues/472)) ([da7e377](https://github.com/YrrepNoj/leapfrogai-test/commit/da7e37700b8a19a34e92109f1a8479c0b681146f))
* make sure pytest catches files ([#438](https://github.com/YrrepNoj/leapfrogai-test/issues/438)) ([fe3bd9b](https://github.com/YrrepNoj/leapfrogai-test/commit/fe3bd9b05bd9df6e82e6db976acadfbab855297d))
* Quality of Life issues ([#429](https://github.com/YrrepNoj/leapfrogai-test/issues/429)) ([5f5444b](https://github.com/YrrepNoj/leapfrogai-test/commit/5f5444baf238c09af65f977c1c8e187121da3809))
* send and cancel btn tooltips ([#436](https://github.com/YrrepNoj/leapfrogai-test/issues/436)) ([bbb6ea9](https://github.com/YrrepNoj/leapfrogai-test/commit/bbb6ea9f7a8a45a67af4c7989c569b66aa388b6b))
* skip simple test ([610daf4](https://github.com/YrrepNoj/leapfrogai-test/commit/610daf4417c0e854b0bdc24cee6a27e43770be0c))
* update 'latest' bundles to reference ui and supabase via reposistory instead of path ([#508](https://github.com/YrrepNoj/leapfrogai-test/issues/508)) ([818f55a](https://github.com/YrrepNoj/leapfrogai-test/commit/818f55ab8c0d173355345f58f46e36dca7f9e51b))
* update the keycloak url that supabase redirects to ([#535](https://github.com/YrrepNoj/leapfrogai-test/issues/535)) ([541c7bd](https://github.com/YrrepNoj/leapfrogai-test/commit/541c7bdf82aa8dc94dbb1113ecfeb0f075f5b260))
* use zarf vendored kubectl during supabase deployment ([#517](https://github.com/YrrepNoj/leapfrogai-test/issues/517)) ([c236d39](https://github.com/YrrepNoj/leapfrogai-test/commit/c236d39a62694d7750ebe562b2f55dcafc238d34))


### Miscellaneous

* add CODEOWNERS to repository ([#269](https://github.com/YrrepNoj/leapfrogai-test/issues/269)) ([b08dbed](https://github.com/YrrepNoj/leapfrogai-test/commit/b08dbed0a858ec68d469e9eeb1966b02a2d97cce))
* Add RAG Evals Toolset ADR ([#529](https://github.com/YrrepNoj/leapfrogai-test/issues/529)) ([840f49a](https://github.com/YrrepNoj/leapfrogai-test/commit/840f49a1ecc7695fb96afd35c5a6c2097a77c581))
* add zarf variable to api package for exposing the OpenAPI specification ([#503](https://github.com/YrrepNoj/leapfrogai-test/issues/503)) ([054444c](https://github.com/YrrepNoj/leapfrogai-test/commit/054444c8dd6770c5cf4cacfcb3495db09533b82d))
* add zarf yaml schema and set useful component names ([#373](https://github.com/YrrepNoj/leapfrogai-test/issues/373)) ([ae618ca](https://github.com/YrrepNoj/leapfrogai-test/commit/ae618cab3c347fbcb07d67e0b434a0d09e15e80e))
* adding huggingface_hub has optional dev dependency ([#440](https://github.com/YrrepNoj/leapfrogai-test/issues/440)) ([857f583](https://github.com/YrrepNoj/leapfrogai-test/commit/857f5838ab7ef5cc4b1545bff4406a616babf211))
* **adr:** vLLM as default main inferencing engine ([4611a45](https://github.com/YrrepNoj/leapfrogai-test/commit/4611a45ca69a88e2ae8f775ec1e60fe1fd180d49))
* bring ui into monorepo ([#349](https://github.com/YrrepNoj/leapfrogai-test/issues/349)) ([0463af9](https://github.com/YrrepNoj/leapfrogai-test/commit/0463af916558bb46c965a7a37b2ef169d1c3a4dc))
* **ci:** Add precommit linting and scorecard workflows ([#270](https://github.com/YrrepNoj/leapfrogai-test/issues/270)) ([dd479f0](https://github.com/YrrepNoj/leapfrogai-test/commit/dd479f0770d3bc72308e683fbf32fa987c25df55))
* **ci:** add unit test and linting workflow for leapfrogai_ui ([#439](https://github.com/YrrepNoj/leapfrogai-test/issues/439)) ([b5aa668](https://github.com/YrrepNoj/leapfrogai-test/commit/b5aa668df38b6149d009ae663e39deefa01455ce))
* **ci:** always run the pytest workflow ([#379](https://github.com/YrrepNoj/leapfrogai-test/issues/379)) ([1a6f29e](https://github.com/YrrepNoj/leapfrogai-test/commit/1a6f29e5d4bba9a73e917241d232a341b79ec28f))
* **ci:** setup release-please to assist with manage version refs internally ([#465](https://github.com/YrrepNoj/leapfrogai-test/issues/465)) ([8c300b0](https://github.com/YrrepNoj/leapfrogai-test/commit/8c300b0b8d25c9a96a9915d41922066509292957))
* **ci:** update publish workflow w leapfrogai UI artifacts ([#464](https://github.com/YrrepNoj/leapfrogai-test/issues/464)) ([32c4ab5](https://github.com/YrrepNoj/leapfrogai-test/commit/32c4ab5e2a37fb086b9925397c510965af1b0b47))
* cleanup todo comments throughout the codebase ([#375](https://github.com/YrrepNoj/leapfrogai-test/issues/375)) ([1aec77b](https://github.com/YrrepNoj/leapfrogai-test/commit/1aec77b6778a3c9a6bce7da291f9c11a88bed9cd))
* Conform version numbers prior to release ([#382](https://github.com/YrrepNoj/leapfrogai-test/issues/382)) ([86ac1f3](https://github.com/YrrepNoj/leapfrogai-test/commit/86ac1f36ffdea433584d49badc22ff495188476d))
* Consolidate our repos into a monorepo ([#268](https://github.com/YrrepNoj/leapfrogai-test/issues/268)) ([70e0bdf](https://github.com/YrrepNoj/leapfrogai-test/commit/70e0bdfd659169174d6e6dfb7864faded7ab0d00))
* create issue template for new feature requests ([#348](https://github.com/YrrepNoj/leapfrogai-test/issues/348)) ([7b5d564](https://github.com/YrrepNoj/leapfrogai-test/commit/7b5d56464d4ec11df53eea77707c377fdf2344e1))
* create shim e2e workflow ([#377](https://github.com/YrrepNoj/leapfrogai-test/issues/377)) ([904ef22](https://github.com/YrrepNoj/leapfrogai-test/commit/904ef2245072226ecd77636343a35b308fbadf1c))
* **deps-dev:** bump @sveltejs/kit in /src/leapfrogai_ui ([#452](https://github.com/YrrepNoj/leapfrogai-test/issues/452)) ([d2553fe](https://github.com/YrrepNoj/leapfrogai-test/commit/d2553fe249e1d3de54be982ae8b680bab9d6dc98))
* **deps-dev:** bump @testing-library/svelte in /src/leapfrogai_ui ([#449](https://github.com/YrrepNoj/leapfrogai-test/issues/449)) ([e3d6a45](https://github.com/YrrepNoj/leapfrogai-test/commit/e3d6a45696ca39e08a5db154277446d4a05fb39b))
* **deps-dev:** bump @typescript-eslint/parser in /src/leapfrogai_ui ([#427](https://github.com/YrrepNoj/leapfrogai-test/issues/427)) ([a8be49b](https://github.com/YrrepNoj/leapfrogai-test/commit/a8be49bb0cbca30d7429e444bbdb94bdfa1837e0))
* **deps-dev:** bump eslint-plugin-svelte in /src/leapfrogai_ui ([#477](https://github.com/YrrepNoj/leapfrogai-test/issues/477)) ([9666a79](https://github.com/YrrepNoj/leapfrogai-test/commit/9666a79d82feedbec0fb7bdc15a85e4cc3a3ab58))
* **deps-dev:** bump svelte from 4.2.12 to 4.2.15 in /src/leapfrogai_ui ([#451](https://github.com/YrrepNoj/leapfrogai-test/issues/451)) ([62cb193](https://github.com/YrrepNoj/leapfrogai-test/commit/62cb19318e5d60ffb2fd3f1e5352dd2409bf09ba))
* **deps-dev:** bump svelte-check in /src/leapfrogai_ui ([#475](https://github.com/YrrepNoj/leapfrogai-test/issues/475)) ([21be2a1](https://github.com/YrrepNoj/leapfrogai-test/commit/21be2a19e43af2aacf23c48d62080777c8ac38a7))
* **deps-dev:** bump typescript in /src/leapfrogai_ui ([#478](https://github.com/YrrepNoj/leapfrogai-test/issues/478)) ([5393e34](https://github.com/YrrepNoj/leapfrogai-test/commit/5393e34b42a727d5b53b4d5dcc678cecc900976d))
* **deps-dev:** bump vite from 5.1.5 to 5.2.10 in /src/leapfrogai_ui ([#426](https://github.com/YrrepNoj/leapfrogai-test/issues/426)) ([392c821](https://github.com/YrrepNoj/leapfrogai-test/commit/392c82121faf4a0213524c4b4581c92c875cd26f))
* **deps:** bump @supabase/ssr in /src/leapfrogai_ui ([#476](https://github.com/YrrepNoj/leapfrogai-test/issues/476)) ([49efaec](https://github.com/YrrepNoj/leapfrogai-test/commit/49efaec9aea05e8e5fad3ff94cc0c2ab95efe2bc))
* **deps:** bump @sveltejs/vite-plugin-svelte in /src/leapfrogai_ui ([#453](https://github.com/YrrepNoj/leapfrogai-test/issues/453)) ([06062c8](https://github.com/YrrepNoj/leapfrogai-test/commit/06062c8c8c7bfdd929bcd3e65d80ab864d4290f7))
* **deps:** bump msw from 2.2.3 to 2.2.14 in /src/leapfrogai_ui ([#425](https://github.com/YrrepNoj/leapfrogai-test/issues/425)) ([8cfe8b5](https://github.com/YrrepNoj/leapfrogai-test/commit/8cfe8b5fe13abf09da9f9fa2f3916e96fbd97c3f))
* **deps:** bump openai from 4.29.0 to 4.38.5 in /src/leapfrogai_ui ([#450](https://github.com/YrrepNoj/leapfrogai-test/issues/450)) ([7567bc7](https://github.com/YrrepNoj/leapfrogai-test/commit/7567bc7321de5550b228968af5a58a7458d78b86))
* **deps:** bump openai from 4.38.5 to 4.41.1 in /src/leapfrogai_ui ([#474](https://github.com/YrrepNoj/leapfrogai-test/issues/474)) ([86837e9](https://github.com/YrrepNoj/leapfrogai-test/commit/86837e96c107dcce917d26b1b03268108098c40c))
* documenting proposal for solution to database ADR ([#416](https://github.com/YrrepNoj/leapfrogai-test/issues/416)) ([7a3a0ad](https://github.com/YrrepNoj/leapfrogai-test/commit/7a3a0add9d67fb229ed1f20a8df27bc3ea8f1d84))
* group 'minor' and 'patch' level npm dependency updates ([#547](https://github.com/YrrepNoj/leapfrogai-test/issues/547)) ([064cb84](https://github.com/YrrepNoj/leapfrogai-test/commit/064cb84de7e6711487ffd4b9513b09135cbbf1d4))
* issue templates ([#301](https://github.com/YrrepNoj/leapfrogai-test/issues/301)) ([e417519](https://github.com/YrrepNoj/leapfrogai-test/commit/e41751954caeb9837989cc4392b182bcfdab4e56))
* **main:** release 0.7.0 ([#485](https://github.com/YrrepNoj/leapfrogai-test/issues/485)) ([0e84764](https://github.com/YrrepNoj/leapfrogai-test/commit/0e84764015a6eba4eefcdbc1a98e5c2d345ca293))
* **main:** release 0.7.1 ([#511](https://github.com/YrrepNoj/leapfrogai-test/issues/511)) ([47249c4](https://github.com/YrrepNoj/leapfrogai-test/commit/47249c410feae6352fff134b75174c736d21a09b))
* **main:** release 0.7.2 ([#527](https://github.com/YrrepNoj/leapfrogai-test/issues/527)) ([7ba0e53](https://github.com/YrrepNoj/leapfrogai-test/commit/7ba0e530321c6a4c54cf778adff8e08400d16279))
* Misc UI package configuration updates ([#495](https://github.com/YrrepNoj/leapfrogai-test/issues/495)) ([ebe4fde](https://github.com/YrrepNoj/leapfrogai-test/commit/ebe4fde51217708c0a7535eb7382628ced740abb))
* refactoring API and adding stubs for new OpenAI endpoints ([#437](https://github.com/YrrepNoj/leapfrogai-test/issues/437)) ([cba9676](https://github.com/YrrepNoj/leapfrogai-test/commit/cba967646b3f0e4cabd833b53c51fefaa30cda78))
* reformat with new prettier settings ([#466](https://github.com/YrrepNoj/leapfrogai-test/issues/466)) ([2bfad2d](https://github.com/YrrepNoj/leapfrogai-test/commit/2bfad2dff6d844b7563251fd8dffb447caae5561))
* remove redundant optional dependencies within our pyproject.toml ([#374](https://github.com/YrrepNoj/leapfrogai-test/issues/374)) ([4d394ba](https://github.com/YrrepNoj/leapfrogai-test/commit/4d394baf81d2c1ecd4158292b27b3d1629f44d1d))
* remove unused requirements.txt file ([#546](https://github.com/YrrepNoj/leapfrogai-test/issues/546)) ([e71e74f](https://github.com/YrrepNoj/leapfrogai-test/commit/e71e74fc23b68895ceaddc743db3d4386aa59d7a))
* restrict e2e tests from running on lfai-ui changes ([#401](https://github.com/YrrepNoj/leapfrogai-test/issues/401)) ([037d157](https://github.com/YrrepNoj/leapfrogai-test/commit/037d157895df4592a9f57319b45025fed30a1bb1))
* show copy/edit btns for non last message during regen ([#444](https://github.com/YrrepNoj/leapfrogai-test/issues/444)) ([7c67a4f](https://github.com/YrrepNoj/leapfrogai-test/commit/7c67a4fbf521ec388f7a36512c9aa10e064c380f))
* Supabase migrations ([#496](https://github.com/YrrepNoj/leapfrogai-test/issues/496)) ([86ed880](https://github.com/YrrepNoj/leapfrogai-test/commit/86ed88072b0664619b763eff38e85ec2b040a507))
* Turn supabase domain into a templated value ([#512](https://github.com/YrrepNoj/leapfrogai-test/issues/512)) ([312d587](https://github.com/YrrepNoj/leapfrogai-test/commit/312d5874e7c8fd28f2c50b1b91082e5f25356c08))
* update version refs to 0.6.1 ([#389](https://github.com/YrrepNoj/leapfrogai-test/issues/389)) ([bc06594](https://github.com/YrrepNoj/leapfrogai-test/commit/bc065949ec16de04fb97c88607e8c8e4882b55f0))
* update vllm to use gptq quanitzed model ([#378](https://github.com/YrrepNoj/leapfrogai-test/issues/378)) ([dc1029d](https://github.com/YrrepNoj/leapfrogai-test/commit/dc1029d0d9c1cc7717d592f9cbe8067cf58e9d13))
* updates ruff in linting workflow to 0.3.4 ([#333](https://github.com/YrrepNoj/leapfrogai-test/issues/333)) ([cde009a](https://github.com/YrrepNoj/leapfrogai-test/commit/cde009a3de8fb6d3f8f1e3ca115d85c576e078ae))

## [0.7.2](https://github.com/defenseunicorns/leapfrogai/compare/v0.7.1...v0.7.2) (2024-05-15)


### Bug Fixes

* use zarf vendored kubectl during supabase deployment ([#517](https://github.com/defenseunicorns/leapfrogai/issues/517)) ([c236d39](https://github.com/defenseunicorns/leapfrogai/commit/c236d39a62694d7750ebe562b2f55dcafc238d34))

## [0.7.1](https://github.com/defenseunicorns/leapfrogai/compare/v0.7.0...v0.7.1) (2024-05-15)


### Bug Fixes

* allow release-please to update pyrpoject.toml files ([#509](https://github.com/defenseunicorns/leapfrogai/issues/509)) ([3e1f0a6](https://github.com/defenseunicorns/leapfrogai/commit/3e1f0a6c3a749e868caabf31035ddbbe6831bb1c))
* update 'latest' bundles to reference ui and supabase via reposistory instead of path ([#508](https://github.com/defenseunicorns/leapfrogai/issues/508)) ([818f55a](https://github.com/defenseunicorns/leapfrogai/commit/818f55ab8c0d173355345f58f46e36dca7f9e51b))


### Miscellaneous

* Turn supabase domain into a templated value ([#512](https://github.com/defenseunicorns/leapfrogai/issues/512)) ([312d587](https://github.com/defenseunicorns/leapfrogai/commit/312d5874e7c8fd28f2c50b1b91082e5f25356c08))

## [0.7.0](https://github.com/defenseunicorns/leapfrogai/compare/v0.6.1...v0.7.0) (2024-05-14)


### Features

* Add supabase deployment package ([#380](https://github.com/defenseunicorns/leapfrogai/issues/380)) ([8982bc0](https://github.com/defenseunicorns/leapfrogai/commit/8982bc08e7e2dac496409a38e3f53f7757c3bdbf))
* files endpoints ([#467](https://github.com/defenseunicorns/leapfrogai/issues/467)) ([c269eee](https://github.com/defenseunicorns/leapfrogai/commit/c269eee174124949b103240110bd1eae5177d301))
* sidenav redesign with import and export ([#398](https://github.com/defenseunicorns/leapfrogai/issues/398)) ([368e4e9](https://github.com/defenseunicorns/leapfrogai/commit/368e4e9b152a126a02473dbff46875da94c58d3a))
* textarea instead of text input ([#435](https://github.com/defenseunicorns/leapfrogai/issues/435)) ([47a0fba](https://github.com/defenseunicorns/leapfrogai/commit/47a0fba2196fd3ea67d0190401a9247f1bad5803))
* ui assistants management ([#469](https://github.com/defenseunicorns/leapfrogai/issues/469)) ([28ba7ed](https://github.com/defenseunicorns/leapfrogai/commit/28ba7edd1cdd22eda99b50a3fe08f987cc53e020))
* **ui:** Assistant Avatars ([#494](https://github.com/defenseunicorns/leapfrogai/issues/494)) ([b4d9cfc](https://github.com/defenseunicorns/leapfrogai/commit/b4d9cfc0b2d7b6d89f0efc0d6d76438fd2f9d92e))
* **ui:** dates ([#404](https://github.com/defenseunicorns/leapfrogai/issues/404)) ([7efcebf](https://github.com/defenseunicorns/leapfrogai/commit/7efcebfceac3a3f9670005ebb9ba6ba6e977d94d))


### Bug Fixes

* input resize bug ([#472](https://github.com/defenseunicorns/leapfrogai/issues/472)) ([da7e377](https://github.com/defenseunicorns/leapfrogai/commit/da7e37700b8a19a34e92109f1a8479c0b681146f))
* make sure pytest catches files ([#438](https://github.com/defenseunicorns/leapfrogai/issues/438)) ([fe3bd9b](https://github.com/defenseunicorns/leapfrogai/commit/fe3bd9b05bd9df6e82e6db976acadfbab855297d))
* Quality of Life issues ([#429](https://github.com/defenseunicorns/leapfrogai/issues/429)) ([5f5444b](https://github.com/defenseunicorns/leapfrogai/commit/5f5444baf238c09af65f977c1c8e187121da3809))
* send and cancel btn tooltips ([#436](https://github.com/defenseunicorns/leapfrogai/issues/436)) ([bbb6ea9](https://github.com/defenseunicorns/leapfrogai/commit/bbb6ea9f7a8a45a67af4c7989c569b66aa388b6b))


### Miscellaneous

* add zarf variable to api package for exposing the OpenAPI specification ([#503](https://github.com/defenseunicorns/leapfrogai/issues/503)) ([054444c](https://github.com/defenseunicorns/leapfrogai/commit/054444c8dd6770c5cf4cacfcb3495db09533b82d))
* adding huggingface_hub has optional dev dependency ([#440](https://github.com/defenseunicorns/leapfrogai/issues/440)) ([857f583](https://github.com/defenseunicorns/leapfrogai/commit/857f5838ab7ef5cc4b1545bff4406a616babf211))
* bring ui into monorepo ([#349](https://github.com/defenseunicorns/leapfrogai/issues/349)) ([0463af9](https://github.com/defenseunicorns/leapfrogai/commit/0463af916558bb46c965a7a37b2ef169d1c3a4dc))
* **ci:** add unit test and linting workflow for leapfrogai_ui ([#439](https://github.com/defenseunicorns/leapfrogai/issues/439)) ([b5aa668](https://github.com/defenseunicorns/leapfrogai/commit/b5aa668df38b6149d009ae663e39deefa01455ce))
* **ci:** setup release-please to assist with manage version refs internally ([#465](https://github.com/defenseunicorns/leapfrogai/issues/465)) ([8c300b0](https://github.com/defenseunicorns/leapfrogai/commit/8c300b0b8d25c9a96a9915d41922066509292957))
* **ci:** update publish workflow w leapfrogai UI artifacts ([#464](https://github.com/defenseunicorns/leapfrogai/issues/464)) ([32c4ab5](https://github.com/defenseunicorns/leapfrogai/commit/32c4ab5e2a37fb086b9925397c510965af1b0b47))
* **deps-dev:** bump @sveltejs/kit in /src/leapfrogai_ui ([#452](https://github.com/defenseunicorns/leapfrogai/issues/452)) ([d2553fe](https://github.com/defenseunicorns/leapfrogai/commit/d2553fe249e1d3de54be982ae8b680bab9d6dc98))
* **deps-dev:** bump @testing-library/svelte in /src/leapfrogai_ui ([#449](https://github.com/defenseunicorns/leapfrogai/issues/449)) ([e3d6a45](https://github.com/defenseunicorns/leapfrogai/commit/e3d6a45696ca39e08a5db154277446d4a05fb39b))
* **deps-dev:** bump @typescript-eslint/parser in /src/leapfrogai_ui ([#427](https://github.com/defenseunicorns/leapfrogai/issues/427)) ([a8be49b](https://github.com/defenseunicorns/leapfrogai/commit/a8be49bb0cbca30d7429e444bbdb94bdfa1837e0))
* **deps-dev:** bump eslint-plugin-svelte in /src/leapfrogai_ui ([#477](https://github.com/defenseunicorns/leapfrogai/issues/477)) ([9666a79](https://github.com/defenseunicorns/leapfrogai/commit/9666a79d82feedbec0fb7bdc15a85e4cc3a3ab58))
* **deps-dev:** bump svelte from 4.2.12 to 4.2.15 in /src/leapfrogai_ui ([#451](https://github.com/defenseunicorns/leapfrogai/issues/451)) ([62cb193](https://github.com/defenseunicorns/leapfrogai/commit/62cb19318e5d60ffb2fd3f1e5352dd2409bf09ba))
* **deps-dev:** bump svelte-check in /src/leapfrogai_ui ([#475](https://github.com/defenseunicorns/leapfrogai/issues/475)) ([21be2a1](https://github.com/defenseunicorns/leapfrogai/commit/21be2a19e43af2aacf23c48d62080777c8ac38a7))
* **deps-dev:** bump typescript in /src/leapfrogai_ui ([#478](https://github.com/defenseunicorns/leapfrogai/issues/478)) ([5393e34](https://github.com/defenseunicorns/leapfrogai/commit/5393e34b42a727d5b53b4d5dcc678cecc900976d))
* **deps-dev:** bump vite from 5.1.5 to 5.2.10 in /src/leapfrogai_ui ([#426](https://github.com/defenseunicorns/leapfrogai/issues/426)) ([392c821](https://github.com/defenseunicorns/leapfrogai/commit/392c82121faf4a0213524c4b4581c92c875cd26f))
* **deps:** bump @supabase/ssr in /src/leapfrogai_ui ([#476](https://github.com/defenseunicorns/leapfrogai/issues/476)) ([49efaec](https://github.com/defenseunicorns/leapfrogai/commit/49efaec9aea05e8e5fad3ff94cc0c2ab95efe2bc))
* **deps:** bump @sveltejs/vite-plugin-svelte in /src/leapfrogai_ui ([#453](https://github.com/defenseunicorns/leapfrogai/issues/453)) ([06062c8](https://github.com/defenseunicorns/leapfrogai/commit/06062c8c8c7bfdd929bcd3e65d80ab864d4290f7))
* **deps:** bump msw from 2.2.3 to 2.2.14 in /src/leapfrogai_ui ([#425](https://github.com/defenseunicorns/leapfrogai/issues/425)) ([8cfe8b5](https://github.com/defenseunicorns/leapfrogai/commit/8cfe8b5fe13abf09da9f9fa2f3916e96fbd97c3f))
* **deps:** bump openai from 4.29.0 to 4.38.5 in /src/leapfrogai_ui ([#450](https://github.com/defenseunicorns/leapfrogai/issues/450)) ([7567bc7](https://github.com/defenseunicorns/leapfrogai/commit/7567bc7321de5550b228968af5a58a7458d78b86))
* **deps:** bump openai from 4.38.5 to 4.41.1 in /src/leapfrogai_ui ([#474](https://github.com/defenseunicorns/leapfrogai/issues/474)) ([86837e9](https://github.com/defenseunicorns/leapfrogai/commit/86837e96c107dcce917d26b1b03268108098c40c))
* documenting proposal for solution to database ADR ([#416](https://github.com/defenseunicorns/leapfrogai/issues/416)) ([7a3a0ad](https://github.com/defenseunicorns/leapfrogai/commit/7a3a0add9d67fb229ed1f20a8df27bc3ea8f1d84))
* Misc UI package configuration updates ([#495](https://github.com/defenseunicorns/leapfrogai/issues/495)) ([ebe4fde](https://github.com/defenseunicorns/leapfrogai/commit/ebe4fde51217708c0a7535eb7382628ced740abb))
* refactoring API and adding stubs for new OpenAI endpoints ([#437](https://github.com/defenseunicorns/leapfrogai/issues/437)) ([cba9676](https://github.com/defenseunicorns/leapfrogai/commit/cba967646b3f0e4cabd833b53c51fefaa30cda78))
* reformat with new prettier settings ([#466](https://github.com/defenseunicorns/leapfrogai/issues/466)) ([2bfad2d](https://github.com/defenseunicorns/leapfrogai/commit/2bfad2dff6d844b7563251fd8dffb447caae5561))
* restrict e2e tests from running on lfai-ui changes ([#401](https://github.com/defenseunicorns/leapfrogai/issues/401)) ([037d157](https://github.com/defenseunicorns/leapfrogai/commit/037d157895df4592a9f57319b45025fed30a1bb1))
* show copy/edit btns for non last message during regen ([#444](https://github.com/defenseunicorns/leapfrogai/issues/444)) ([7c67a4f](https://github.com/defenseunicorns/leapfrogai/commit/7c67a4fbf521ec388f7a36512c9aa10e064c380f))
* Supabase migrations ([#496](https://github.com/defenseunicorns/leapfrogai/issues/496)) ([86ed880](https://github.com/defenseunicorns/leapfrogai/commit/86ed88072b0664619b763eff38e85ec2b040a507))

## [0.6.1](https://github.com/defenseunicorns/leapfrogai/compare/v0.6.0...v0.6.1) (2024-04-12)

### Features

### Bug Fixes
* fix: remove hardcoded gpu request value by @YrrepNoj in https://github.com/defenseunicorns/leapfrogai/pull/386

### Miscellaneous
* chore: update version refs to 0.6.1 by @YrrepNoj in https://github.com/defenseunicorns/leapfrogai/pull/389


## [0.6.0](https://github.com/defenseunicorns/leapfrogai/releases/tag/v0.6.0) (2024-04-12)

### Features

### Bug Fixes

### Miscellaneous
