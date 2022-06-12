from __future__ import annotations
EXTENSIONS = {
    'adoc': {'text', 'asciidoc'},
    'ai': {'binary', 'adobe-illustrator'},
    'aj': {'text', 'aspectj'},
    'asciidoc': {'text', 'asciidoc'},
    'apinotes': {'text', 'apinotes'},
    'asar': {'binary', 'asar'},
    'avif': {'binary', 'image', 'avif'},
    'bash': {'text', 'shell', 'bash'},
    'bat': {'text', 'batch'},
    'bats': {'text', 'shell', 'bash', 'bats'},
    'bib': {'text', 'bib'},
    'bmp': {'binary', 'image', 'bitmap'},
    'bz2': {'binary', 'bzip2'},
    'bzl': {'text', 'bazel'},
    'c': {'text', 'c'},
    'cc': {'text', 'c++'},
    'cfg': {'text'},
    'chs': {'text', 'c2hs'},
    'cjs': {'text', 'javascript'},
    'clj': {'text', 'clojure'},
    'cljc': {'text', 'clojure'},
    'cljs': {'text', 'clojure', 'clojurescript'},
    'cmake': {'text', 'cmake'},
    'cnf': {'text'},
    'coffee': {'text', 'coffee'},
    'conf': {'text'},
    'cpp': {'text', 'c++'},
    'cr': {'text', 'crystal'},
    'crt': {'text', 'pem'},
    'cs': {'text', 'c#'},
    'csproj': {'text', 'xml', 'csproj'},
    'csh': {'text', 'shell', 'csh'},
    'cson': {'text', 'cson'},
    'css': {'text', 'css'},
    'csv': {'text', 'csv'},
    'cu': {'text', 'cuda'},
    'cuh': {'text', 'cuda'},
    'cxx': {'text', 'c++'},
    'dart': {'text', 'dart'},
    'def': {'text', 'def'},
    'dll': {'binary'},
    'dtd': {'text', 'dtd'},
    'ear': {'binary', 'zip', 'jar'},
    'edn': {'text', 'clojure', 'edn'},
    'ejs': {'text', 'ejs'},
    'eot': {'binary', 'eot'},
    'eps': {'binary', 'eps'},
    'erb': {'text', 'erb'},
    'exe': {'binary'},
    'eyaml': {'text', 'yaml'},
    'feature': {'text', 'gherkin'},
    'fish': {'text', 'fish'},
    'gd': {'text', 'gdscript'},
    'gemspec': {'text', 'ruby'},
    'geojson': {'text', 'geojson', 'json'},
    'gif': {'binary', 'image', 'gif'},
    'go': {'text', 'go'},
    'gotmpl': {'text', 'gotmpl'},
    'gpx': {'text', 'gpx', 'xml'},
    'graphql': {'text', 'graphql'},
    'gradle': {'text', 'groovy'},
    'groovy': {'text', 'groovy'},
    'gyb': {'text', 'gyb'},
    'gyp': {'text', 'gyp', 'python'},
    'gypi': {'text', 'gyp', 'python'},
    'gz': {'binary', 'gzip'},
    'h': {'text', 'header', 'c', 'c++'},
    'hbs': {'text', 'handlebars'},
    'hcl': {'text', 'hcl'},
    'hh': {'text', 'header', 'c++'},
    'hpp': {'text', 'header', 'c++'},
    'hs': {'text', 'haskell'},
    'htm': {'text', 'html'},
    'html': {'text', 'html'},
    'hxx': {'text', 'header', 'c++'},
    'icns': {'binary', 'icns'},
    'ico': {'binary', 'icon'},
    'ics': {'text', 'icalendar'},
    'idl': {'text', 'idl'},
    'idr': {'text', 'idris'},
    'inc': {'text', 'inc'},
    'ini': {'text', 'ini'},
    'inl': {'text', 'inl', 'c++'},
    'ino': {'text', 'ino', 'c++'},
    'inx': {'text', 'xml', 'inx'},
    'ipynb': {'text', 'jupyter'},
    'j2': {'text', 'jinja'},
    'jade': {'text', 'jade'},
    'jar': {'binary', 'zip', 'jar'},
    'java': {'text', 'java'},
    'jenkins': {'text', 'groovy', 'jenkins'},
    'jenkinsfile': {'text', 'groovy', 'jenkins'},
    'jinja': {'text', 'jinja'},
    'jinja2': {'text', 'jinja'},
    'jpeg': {'binary', 'image', 'jpeg'},
    'jpg': {'binary', 'image', 'jpeg'},
    'js': {'text', 'javascript'},
    'json': {'text', 'json'},
    'jsonnet': {'text', 'jsonnet'},
    'json5': {'text', 'json5'},
    'jsx': {'text', 'jsx'},
    'key': {'text', 'pem'},
    'kml': {'text', 'kml', 'xml'},
    'kt': {'text', 'kotlin'},
    'kts': {'text', 'kotlin'},
    'lean': {'text', 'lean'},
    'lektorproject': {'text', 'ini', 'lektorproject'},
    'less': {'text', 'less'},
    'lhs': {'text', 'literate-haskell'},
    'libsonnet': {'text', 'jsonnet'},
    'lidr': {'text', 'idris'},
    'liquid': {'text', 'liquid'},
    'lr': {'text', 'lektor'},
    'lua': {'text', 'lua'},
    'm': {'text', 'objective-c'},
    'manifest': {'text', 'manifest'},
    'map': {'text', 'map'},
    'markdown': {'text', 'markdown'},
    'md': {'text', 'markdown'},
    'mdx': {'text', 'mdx'},
    'mib': {'text', 'mib'},
    'mjs': {'text', 'javascript'},
    'mk': {'text', 'makefile'},
    'ml': {'text', 'ocaml'},
    'mli': {'text', 'ocaml'},
    'mm': {'text', 'c++', 'objective-c++'},
    'modulemap': {'text', 'modulemap'},
    'mscx': {'text', 'xml', 'musescore'},
    'mscz': {'binary', 'zip', 'musescore'},
    'myst': {'text', 'myst'},
    'ngdoc': {'text', 'ngdoc'},
    'nim': {'text', 'nim'},
    'nims': {'text', 'nim'},
    'nimble': {'text', 'nimble'},
    'nix': {'text', 'nix'},
    'njk': {'text', 'nunjucks'},
    'otf': {'binary', 'otf'},
    'p12': {'binary', 'p12'},
    'patch': {'text', 'diff'},
    'pdf': {'binary', 'pdf'},
    'pem': {'text', 'pem'},
    'php': {'text', 'php'},
    'php4': {'text', 'php'},
    'php5': {'text', 'php'},
    'phtml': {'text', 'php'},
    'pl': {'text', 'perl'},
    'plantuml': {'text', 'plantuml'},
    'pm': {'text', 'perl'},
    'png': {'binary', 'image', 'png'},
    'po': {'text', 'pofile'},
    'pp': {'text', 'puppet'},
    'prisma': {'text', 'prisma'},
    'properties': {'text', 'java-properties'},
    'proto': {'text', 'proto'},
    'ps1': {'text', 'powershell'},
    'puml': {'text', 'plantuml'},
    'purs': {'text', 'purescript'},
    'pxd': {'text', 'cython'},
    'pxi': {'text', 'cython'},
    'py': {'text', 'python'},
    'pyi': {'text', 'pyi'},
    'pyproj': {'text', 'xml', 'pyproj'},
    'pyx': {'text', 'cython'},
    'pyz': {'binary', 'pyz'},
    'pyzw': {'binary', 'pyz'},
    'qml': {'text', 'qml'},
    'r': {'text', 'r'},
    'rake': {'text', 'ruby'},
    'rb': {'text', 'ruby'},
    'rng': {'text', 'xml', 'relax-ng'},
    'rs': {'text', 'rust'},
    'rst': {'text', 'rst'},
    's': {'text', 'asm'},
    'sass': {'text', 'sass'},
    'sbt': {'text', 'sbt', 'scala'},
    'sc': {'text', 'scala'},
    'scala': {'text', 'scala'},
    'scm': {'text', 'scheme'},
    'scss': {'text', 'scss'},
    'sh': {'text', 'shell'},
    'sln': {'text', 'sln'},
    'sls': {'text', 'salt'},
    'so': {'binary'},
    'sol': {'text', 'solidity'},
    'spec': {'text', 'spec'},
    'sql': {'text', 'sql'},
    'ss': {'text', 'scheme'},
    'sty': {'text', 'tex'},
    'styl': {'text', 'stylus'},
    'sv': {'text', 'system-verilog'},
    'svelte': {'text', 'svelte'},
    'svg': {'text', 'image', 'svg', 'xml'},
    'svh': {'text', 'system-verilog'},
    'swf': {'binary', 'swf'},
    'swift': {'text', 'swift'},
    'swiftdeps': {'text', 'swiftdeps'},
    'tac': {'text', 'twisted', 'python'},
    'tar': {'binary', 'tar'},
    'tex': {'text', 'tex'},
    'tf': {'text', 'terraform'},
    'tfvars': {'text', 'terraform'},
    'tgz': {'binary', 'gzip'},
    'thrift': {'text', 'thrift'},
    'tiff': {'binary', 'image', 'tiff'},
    'toml': {'text', 'toml'},
    'ts': {'text', 'ts'},
    'tsv': {'text', 'tsv'},
    'tsx': {'text', 'tsx'},
    'ttf': {'binary', 'ttf'},
    'twig': {'text', 'twig'},
    'txsprofile': {'text', 'ini', 'txsprofile'},
    'txt': {'text', 'plain-text'},
    'urdf': {'text', 'xml', 'urdf'},
    'v': {'text', 'verilog'},
    'vb': {'text', 'vb'},
    'vbproj': {'text', 'xml', 'vbproj'},
    'vcxproj': {'text', 'xml', 'vcxproj'},
    'vdx': {'text', 'vdx'},
    'vh': {'text', 'verilog'},
    'vhd': {'text', 'vhdl'},
    'vim': {'text', 'vim'},
    'vtl': {'text', 'vtl'},
    'vue': {'text', 'vue'},
    'war': {'binary', 'zip', 'jar'},
    'wav': {'binary', 'audio', 'wav'},
    'webp': {'binary', 'image', 'webp'},
    'whl': {'binary', 'wheel', 'zip'},
    'wkt': {'text', 'wkt'},
    'woff': {'binary', 'woff'},
    'woff2': {'binary', 'woff2'},
    'wsgi': {'text', 'wsgi', 'python'},
    'xhtml': {'text', 'xml', 'html', 'xhtml'},
    'xml': {'text', 'xml'},
    'xq': {'text', 'xquery'},
    'xql': {'text', 'xquery'},
    'xqm': {'text', 'xquery'},
    'xqu': {'text', 'xquery'},
    'xquery': {'text', 'xquery'},
    'xqy': {'text', 'xquery'},
    'xsd': {'text', 'xml', 'xsd'},
    'xsl': {'text', 'xml', 'xsl'},
    'yaml': {'text', 'yaml'},
    'yang': {'text', 'yang'},
    'yin': {'text', 'xml', 'yin'},
    'yml': {'text', 'yaml'},
    'zcml': {'text', 'xml', 'zcml'},
    'zig': {'text', 'zig'},
    'zip': {'binary', 'zip'},
    'zpt': {'text', 'zpt'},
    'zsh': {'text', 'shell', 'zsh'},
}
EXTENSIONS_NEED_BINARY_CHECK = {
    'plist': {'plist'},
}

NAMES = {
    '.babelrc': EXTENSIONS['json'] | {'babelrc'},
    '.bash_aliases': EXTENSIONS['bash'],
    '.bash_profile': EXTENSIONS['bash'],
    '.bashrc': EXTENSIONS['bash'],
    '.bazelrc': {'text', 'bazelrc'},
    '.bowerrc': EXTENSIONS['json'] | {'bowerrc'},
    '.browserslistrc': {'text', 'browserslistrc'},
    '.clang-format': EXTENSIONS['yaml'],
    '.clang-tidy': EXTENSIONS['yaml'],
    '.codespellrc': EXTENSIONS['ini'] | {'codespellrc'},
    '.coveragerc': EXTENSIONS['ini'] | {'coveragerc'},
    '.cshrc': EXTENSIONS['csh'],
    '.csslintrc': EXTENSIONS['json'] | {'csslintrc'},
    '.dockerignore': {'text', 'dockerignore'},
    '.editorconfig': EXTENSIONS['ini'] | {'editorconfig'},
    '.flake8': EXTENSIONS['ini'] | {'flake8'},
    '.gitattributes': {'text', 'gitattributes'},
    '.gitconfig': EXTENSIONS['ini'] | {'gitconfig'},
    '.gitignore': {'text', 'gitignore'},
    '.gitlint': EXTENSIONS['ini'] | {'gitlint'},
    '.gitmodules': {'text', 'gitmodules'},
    '.hgrc': EXTENSIONS['ini'] | {'hgrc'},
    '.jshintrc': EXTENSIONS['json'] | {'jshintrc'},
    '.mailmap': {'text', 'mailmap'},
    '.mention-bot': EXTENSIONS['json'] | {'mention-bot'},
    '.npmignore': {'text', 'npmignore'},
    '.pdbrc': EXTENSIONS['py'] | {'pdbrc'},
    '.prettierignore': {'text', 'gitignore', 'prettierignore'},
    '.pypirc': EXTENSIONS['ini'] | {'pypirc'},
    '.rstcheck.cfg': EXTENSIONS['ini'],
    '.yamllint': EXTENSIONS['yaml'] | {'yamllint'},
    '.zlogin': EXTENSIONS['zsh'],
    '.zlogout': EXTENSIONS['zsh'],
    '.zprofile': EXTENSIONS['zsh'],
    '.zshrc': EXTENSIONS['zsh'],
    '.zshenv': EXTENSIONS['zsh'],
    'AUTHORS': EXTENSIONS['txt'],
    'BUILD': EXTENSIONS['bzl'],
    'BUILD.bazel': EXTENSIONS['bzl'],
    'CMakeLists.txt': EXTENSIONS['cmake'],
    'CHANGELOG': EXTENSIONS['txt'],
    'CONTRIBUTING': EXTENSIONS['txt'],
    'COPYING': EXTENSIONS['txt'],
    'Dockerfile': {'text', 'dockerfile'},
    'Gemfile': EXTENSIONS['rb'],
    'Gemfile.lock': {'text'},
    'GNUmakefile': EXTENSIONS['mk'],
    'go.mod': {'text', 'go-mod'},
    'go.sum': {'text', 'go-sum'},
    'Jenkinsfile': EXTENSIONS['jenkins'],
    'LICENSE': EXTENSIONS['txt'],
    'MAINTAINERS': EXTENSIONS['txt'],
    'Makefile': EXTENSIONS['mk'],
    'makefile': EXTENSIONS['mk'],
    'NEWS': EXTENSIONS['txt'],
    'NOTICE': EXTENSIONS['txt'],
    'PATENTS': EXTENSIONS['txt'],
    'Pipfile': EXTENSIONS['toml'],
    'Pipfile.lock': EXTENSIONS['json'],
    'PKGBUILD': {'text', 'bash', 'pkgbuild', 'alpm'},
    'poetry.lock': EXTENSIONS['toml'],
    'pylintrc': EXTENSIONS['ini'] | {'pylintrc'},
    'README': EXTENSIONS['txt'],
    'Rakefile': EXTENSIONS['rb'],
    'setup.cfg': EXTENSIONS['ini'],
    'WORKSPACE': EXTENSIONS['bzl'],
    'wscript': EXTENSIONS['py'],
}
