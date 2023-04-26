# zaws - Zerapix aws supplemental dev tools

This is a self-updating wrapper for `py-zaws`, which has a number of supplemental dev-toosl.

After installing this, for relevant docs about how to use the tool, go to:

https://github.com/zerapix/py-zaws


## Install

**Important:** If you manually installed a previous version of `py-zaws`, you need to first remove any alias/shell-function for it
before using the installation method below.

Run this in terminal:

```shell
curl -sSL -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/zerapix/bin-zaws/main/bin/download | bash
```

This will download/clone the `bin-zaws`, which is a self-updating wrapper around `py-zaws`.

It will install a sym-link into `~/.local/bin/zaws`, which should already be in your shell-path,
since that's also where `poetry` installs its sym-link too.

After the above command runs, you should be able execute 'zaws' from anywhere; example:

```shell
zaws help
```

After installing this, for relevant docs about how to use the tool, go to:

https://github.com/zerapix/py-zaws

