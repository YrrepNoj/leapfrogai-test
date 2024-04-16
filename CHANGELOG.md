# Changelog

## [0.7.1](https://github.com/YrrepNoj/leapfrogai-test/compare/v0.7.0...v0.7.1) (2024-04-16)


### Miscellaneous

* attempt to switch release-please to draft PRs ([05e858f](https://github.com/YrrepNoj/leapfrogai-test/commit/05e858f8e3299887a2c70e71e4ce89b21a313d1c))
* try to return to blob extra-files ([f2f93f9](https://github.com/YrrepNoj/leapfrogai-test/commit/f2f93f9108a60b11a16b5baef3018a4ac4baf7f5))
* turn yaml extra-files to generic in release-please-config ([34942a1](https://github.com/YrrepNoj/leapfrogai-test/commit/34942a1a36cb9cfc1f7338ce4796907bbca5f6cb))

## [0.7.0](https://github.com/YrrepNoj/leapfrogai-test/compare/v0.6.1...v0.7.0) (2024-04-16)


### Features

* add chat and completion pbs ([5e8dd4b](https://github.com/YrrepNoj/leapfrogai-test/commit/5e8dd4b83b17e920d8a8d1e15f88618dd8b86d79))
* add chat proto and mpt model impl ([f537f26](https://github.com/YrrepNoj/leapfrogai-test/commit/f537f26366cb05698f75fcf2cc02552208205115))
* add working embedding endpoint for all-minilm-l6-v2 ([a03187a](https://github.com/YrrepNoj/leapfrogai-test/commit/a03187a47905e1eec2af8f53fdba07761b6a4586))
* add working HF chat model for mpt-7b-chat ([0d5d818](https://github.com/YrrepNoj/leapfrogai-test/commit/0d5d818f7e730dc5941938351946adc8ce0f15d0))
* factor chat proto into separate services for steam and non-stream ([1bbabb9](https://github.com/YrrepNoj/leapfrogai-test/commit/1bbabb937fc2199050b955f2a4cfde1107059681))
* factor the api code into files for each endpoint ([536c9eb](https://github.com/YrrepNoj/leapfrogai-test/commit/536c9eb7bd021b90696afe3cc12401f6ae7fd105))
* finish renaming completion + generation protos ([9746419](https://github.com/YrrepNoj/leapfrogai-test/commit/974641932cf3861663ad868a5f7e64f803eab9b2))
* fix gitignore to exclude local model files ([2127ed8](https://github.com/YrrepNoj/leapfrogai-test/commit/2127ed82f4fd6de1501aba21b0c648d1091bb35a))
* LLM Backend ADR and ADR Template ([#262](https://github.com/YrrepNoj/leapfrogai-test/issues/262)) ([ff278c2](https://github.com/YrrepNoj/leapfrogai-test/commit/ff278c21b081785a6b82e3104a768a70b2b778de))
* remove pytorch and nvidia dependencies that are already included in our base image ([6a9a4d4](https://github.com/YrrepNoj/leapfrogai-test/commit/6a9a4d4074354023684e5465229f03dc776597b1))
* rename chat.proto's CompletionChoice to ChatCompletionChoice ([50a62b5](https://github.com/YrrepNoj/leapfrogai-test/commit/50a62b5e34795e2ee01c37248607bc3b92654cd6))
* renamed generate endpoint to completion ([b320868](https://github.com/YrrepNoj/leapfrogai-test/commit/b32086888bf1ee83f24f316f2bc3c5ae89f6ae6f))
* update tests to not use the response.text field ([ba626dd](https://github.com/YrrepNoj/leapfrogai-test/commit/ba626ddcc11e6504981fca2b2a11b63d339ea57f))
* updated chat completion proto ([0e7a46c](https://github.com/YrrepNoj/leapfrogai-test/commit/0e7a46cce4e94736d6cfc0ec936c7001ea39b299))
* working container for mpt-chat model ([34130c5](https://github.com/YrrepNoj/leapfrogai-test/commit/34130c5cd1d590720307bd36bdee4baf66d3f8e5))
* working huggingchat api compatibility ([0fbfd17](https://github.com/YrrepNoj/leapfrogai-test/commit/0fbfd171c3d186c6dea46951e51936ff5e38b77d))
* working implementation of streaming + non-streaming chat endpoint ([8c53d88](https://github.com/YrrepNoj/leapfrogai-test/commit/8c53d88e4722d771578cf2c45db0c23034e3dbd8))


### Bug Fixes

* cleanup for pr ([8b3fd50](https://github.com/YrrepNoj/leapfrogai-test/commit/8b3fd5052864316c5aaefc75f7eca77378d03b37))
* correct typos in e2e workflow path triggers ([#376](https://github.com/YrrepNoj/leapfrogai-test/issues/376)) ([ab29743](https://github.com/YrrepNoj/leapfrogai-test/commit/ab297431d2d5acb26b4d6f5c3e231e904b0b7e76))
* fix path to .release-please-manifest.json in tag workflow ([ad49052](https://github.com/YrrepNoj/leapfrogai-test/commit/ad49052a6ebbc3b0d1317a3149d849a69ffa37bb))
* fix release workflow from calling the wrong make target ([#383](https://github.com/YrrepNoj/leapfrogai-test/issues/383)) ([7b4dc7c](https://github.com/YrrepNoj/leapfrogai-test/commit/7b4dc7c658afc7ca7118dacb781d2451d82d6cab))
* skip simple test ([610daf4](https://github.com/YrrepNoj/leapfrogai-test/commit/610daf4417c0e854b0bdc24cee6a27e43770be0c))


### Miscellaneous

* add CODEOWNERS to repository ([#269](https://github.com/YrrepNoj/leapfrogai-test/issues/269)) ([b08dbed](https://github.com/YrrepNoj/leapfrogai-test/commit/b08dbed0a858ec68d469e9eeb1966b02a2d97cce))
* Add release please ([#1](https://github.com/YrrepNoj/leapfrogai-test/issues/1)) ([79a15c8](https://github.com/YrrepNoj/leapfrogai-test/commit/79a15c85c706b1c922541927916dd0b64a22fc61))
* add zarf yaml schema and set useful component names ([#373](https://github.com/YrrepNoj/leapfrogai-test/issues/373)) ([ae618ca](https://github.com/YrrepNoj/leapfrogai-test/commit/ae618cab3c347fbcb07d67e0b434a0d09e15e80e))
* **adr:** vLLM as default main inferencing engine ([4611a45](https://github.com/YrrepNoj/leapfrogai-test/commit/4611a45ca69a88e2ae8f775ec1e60fe1fd180d49))
* bring ui into monorepo ([#349](https://github.com/YrrepNoj/leapfrogai-test/issues/349)) ([0463af9](https://github.com/YrrepNoj/leapfrogai-test/commit/0463af916558bb46c965a7a37b2ef169d1c3a4dc))
* **ci:** Add precommit linting and scorecard workflows ([#270](https://github.com/YrrepNoj/leapfrogai-test/issues/270)) ([dd479f0](https://github.com/YrrepNoj/leapfrogai-test/commit/dd479f0770d3bc72308e683fbf32fa987c25df55))
* **ci:** always run the pytest workflow ([#379](https://github.com/YrrepNoj/leapfrogai-test/issues/379)) ([1a6f29e](https://github.com/YrrepNoj/leapfrogai-test/commit/1a6f29e5d4bba9a73e917241d232a341b79ec28f))
* cleanup todo comments throughout the codebase ([#375](https://github.com/YrrepNoj/leapfrogai-test/issues/375)) ([1aec77b](https://github.com/YrrepNoj/leapfrogai-test/commit/1aec77b6778a3c9a6bce7da291f9c11a88bed9cd))
* Conform version numbers prior to release ([#382](https://github.com/YrrepNoj/leapfrogai-test/issues/382)) ([86ac1f3](https://github.com/YrrepNoj/leapfrogai-test/commit/86ac1f36ffdea433584d49badc22ff495188476d))
* Consolidate our repos into a monorepo ([#268](https://github.com/YrrepNoj/leapfrogai-test/issues/268)) ([70e0bdf](https://github.com/YrrepNoj/leapfrogai-test/commit/70e0bdfd659169174d6e6dfb7864faded7ab0d00))
* create issue template for new feature requests ([#348](https://github.com/YrrepNoj/leapfrogai-test/issues/348)) ([7b5d564](https://github.com/YrrepNoj/leapfrogai-test/commit/7b5d56464d4ec11df53eea77707c377fdf2344e1))
* create shim e2e workflow ([#377](https://github.com/YrrepNoj/leapfrogai-test/issues/377)) ([904ef22](https://github.com/YrrepNoj/leapfrogai-test/commit/904ef2245072226ecd77636343a35b308fbadf1c))
* issue templates ([#301](https://github.com/YrrepNoj/leapfrogai-test/issues/301)) ([e417519](https://github.com/YrrepNoj/leapfrogai-test/commit/e41751954caeb9837989cc4392b182bcfdab4e56))
* remove redundant optional dependencies within our pyproject.toml ([#374](https://github.com/YrrepNoj/leapfrogai-test/issues/374)) ([4d394ba](https://github.com/YrrepNoj/leapfrogai-test/commit/4d394baf81d2c1ecd4158292b27b3d1629f44d1d))
* switch to explicit extra-files paths ([583834c](https://github.com/YrrepNoj/leapfrogai-test/commit/583834c79d40b1ae854606cc3f656a5ff2e669e1))
* update version refs to 0.6.1 ([#389](https://github.com/YrrepNoj/leapfrogai-test/issues/389)) ([bc06594](https://github.com/YrrepNoj/leapfrogai-test/commit/bc065949ec16de04fb97c88607e8c8e4882b55f0))
* update vllm to use gptq quanitzed model ([#378](https://github.com/YrrepNoj/leapfrogai-test/issues/378)) ([dc1029d](https://github.com/YrrepNoj/leapfrogai-test/commit/dc1029d0d9c1cc7717d592f9cbe8067cf58e9d13))
* updates ruff in linting workflow to 0.3.4 ([#333](https://github.com/YrrepNoj/leapfrogai-test/issues/333)) ([cde009a](https://github.com/YrrepNoj/leapfrogai-test/commit/cde009a3de8fb6d3f8f1e3ca115d85c576e078ae))
