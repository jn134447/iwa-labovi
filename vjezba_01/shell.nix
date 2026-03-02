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
    python315
  ];
}
