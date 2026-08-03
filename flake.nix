{
  description = "DevShell for Python.";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    {
      self,
      nixpkgs,
    }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        # Add packages here.
        buildInputs = with pkgs; [
          (pkgs.python3.withPackages (
            python-pkgs: with python-pkgs; [
              # Python packages:
            ]
          ))
          litecli
          python313
          sqlite
          stdenv.cc.cc.lib
          zlib
        ];
        LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib";

        # Shell hooks.
        shellHook = ''
          echo "Entering the development environment!"
        '';
      };
    };
}
