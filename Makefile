doc:
	@uvx --from sphinx \
      --with sphinx-copybutton \
      --with sphinx-design \
      --with sphinx-new-tab-link \
      --with sphinxext-opengraph \
      sphinx-build -M html docs/source docs/build

init:
	@uvx --from sphinx sphinx-quickstart docs \
      -q \
      -p 'pytest TDD workshop' \
      -a nikkie \
      -v '' \
      -l ja \
      --sep \
      --no-makefile \
      --no-batchfile \
      --ext-githubpages \
	--extensions sphinx_copybutton \
      --extensions sphinx_design \
      --extensions sphinx_new_tab_link \
      --extensions sphinxext.opengraph
