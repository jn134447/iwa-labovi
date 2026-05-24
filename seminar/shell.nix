# NOTE: i did not use this as i did programming on windows

let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = with pkgs; [
    nixfmt
    nixd
    nil

    # python314

    ruff
    ty
    uv
  ];
}
