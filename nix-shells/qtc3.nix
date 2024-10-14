let
  pkgs = import <nixpkgs> {};

in pkgs.mkShell {
  packages = [
  	#pkgs.sioyek
  	pkgs.which
  	pkgs.conda
    (pkgs.python3.withPackages (python-pkgs: [
      #python-pkgs.jupyterlab-server
      python-pkgs.qtconsole
      python-pkgs.pyqt5
      python-pkgs.pip
      python-pkgs.matplotlib
    ]))
  ];

  #services.xserver.enable=true;
  #nativeBuildInputs = [ "wrapQtAppsHook" ];
  QT_QPA_PLATFORM="xcb";
  # QT_QPA_PLATFORM="wayland";
  # DISPLAY=":2";
  #QT_QPA_PLATFORM_PLUGIN_PATH="${qt5.qtbase.bin}/lib/qt-${qt5.qtbase.version}/plugins/#platforms";
  #QT_QPA_PLATFORM_PLUGIN_PATH="/nix/store/p15zcalsmqmay3vqq3dd6n7a8pxs78nv-qtbase-5.15.11-bin/lib/qt-5.15.11/plugins/platforms";
  #QT_QPA_PLATFORM_PLUGIN_PATH="/nix/store/dw2iadyxy009bidf85fw9hpcq3zyiqdm-qtbase-5.15.12-bin/lib/qt-5.15.12/plugins/platforms";
  QT_QPA_PLATFORM_PLUGIN_PATH="/nix/store/a2xfqw6rkzxlqlqnhdkx5shby0vl9npf-qtbase-5.15.12-bin/lib/qt-5.15.12/plugins/platforms";
    shellHook = ''
	echo "teste"
	alias qtc="jupyter-qtconsole --JupyterWidget.font_size=16 --JupyterWidget.font_family='SauceCodePro Nerd Font Mono' --JupyterWidget.scrollbar_visibility=False &"
  '';
}
