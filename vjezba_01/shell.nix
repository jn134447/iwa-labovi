{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  packages = with pkgs; [
    nixfmt
    nixd
    nil

    ruff
    ty
    uv
    python313
    python313Packages.debugpy
  ];
}
