# NOTE: i did not use this as i did programming on windows
 
let
  oldpkgs =
    import
      (fetchTarball "https://github.com/NixOS/nixpkgs/archive/06278c77b5d162e62df170fec307e83f1812d94b.tar.gz")
      { };
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages =
    with pkgs;
    [
      nixfmt
      nixd
      nil

      ruff
      ty
      uv
    ]
    ++ [
      oldpkgs.python38Packages.mysql-connector
      oldpkgs.python38
    ];
}
