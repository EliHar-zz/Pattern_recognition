local site_config = {}

site_config.LUAROCKS_PREFIX=[[/root/torch/install/]]
site_config.LUA_INCDIR=[[/root/torch/install/include]]
site_config.LUA_LIBDIR=[[/root/torch/install/lib]]
site_config.LUA_BINDIR=[[/root/torch/install/bin]]
site_config.LUA_INTERPRETER = [[luajit]]
site_config.LUAROCKS_SYSCONFDIR=[[/root/torch/install/etc/luarocks]]
site_config.LUAROCKS_ROCKS_TREE=[[/root/torch/install/]]
site_config.LUAROCKS_ROCKS_SUBDIR=[[lib/luarocks/rocks]]
site_config.LUA_DIR_SET = true
site_config.LUAROCKS_UNAME_S=[[Linux]]
site_config.LUAROCKS_UNAME_M=[[x86_64]]
site_config.LUAROCKS_DOWNLOADER=[[curl]]
site_config.LUAROCKS_MD5CHECKER=[[md5sum]]

return site_config
