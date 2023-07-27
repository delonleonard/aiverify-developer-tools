.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: clone-aiverify
clone-aiverify: # Clone aioverify repo during setup
	@git clone git@github.com:delonleonard/aiverify.git && \
	cd aiverify && \
	git checkout plugin/grad-cam && \
	git sparse-checkout init && git sparse-checkout set ai-verify-shared-library test-engine-core-modules test-engine-core

.PHONY: docker-build
docker-build: # Build docker image from docker/dev.Dockerfile
	DOCKER_BUILDKIT=1 docker build -t aiverify_gram_cam -f docker/dev.Dockerfile .

.PHONY: setup-dev
setup-dev: # Setup dev environment 1. add __init__.py to work aiverify source code rather than install it 
	[ -f template_plugin/algorithms/grad_cam/tests/__init__.py ] || touch template_plugin/algorithms/grad_cam/tests/__init__.py

.PHONY: clean
clean: # Clean up artefact
	find . | grep -E "(__pycache__|\\.pyc|\\.pyo$)" | xargs rm -rf
	find . | grep -E "(.pytest_cache|\\.pyc|\\.pyo$)" | xargs rm -rf


.PHONY: test-dev
test-dev: # Test plugin using template-plugin
	cd template_plugin/algorithms/grad_cam && \
	PYTHONPATH=/workspace/aiverify/test-engine-core:/workspace/aiverify-developer-tools/grad-cam/algorithms/grad-cam:/workspace/template_plugin/algorithms/grad_cam/tests python .
