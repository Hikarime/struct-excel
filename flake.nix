{
  description = "DevShell for Python.";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = {
    self,
    nixpkgs,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {inherit system;};
  in {
    devShells.${system}.default = pkgs.mkShell {
      # Add packages here.
      buildInputs = with pkgs; [
        python313
        (pkgs.python3.withPackages (python-pkgs:
          with python-pkgs; [
            # Python packages:
          ]))
      ];

      # Shell hooks.
      shellHook = ''
        echo "Entering the development environment!"
      '';
    };
  };
}
