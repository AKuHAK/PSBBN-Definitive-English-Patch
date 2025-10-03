{
  description = "PSBBN Definitive English Patch env";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        psbbn = pkgs.writeScriptBin "psbbn" ''
          #!${pkgs.bash}/bin/bash
          ${builtins.concatStringsSep "\n" (
            builtins.tail (pkgs.lib.splitString "\n" (builtins.readFile ../../PSBBN-Definitive-Patch.sh))
          )}
        '';

        pkgs = import nixpkgs { inherit system; };
        pythonEnv = pkgs.python3.withPackages (
          ps: with ps; [
            pip
            lz4
            natsort
            mutagen
            tqdm
          ]
        );
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            bash
            pythonEnv
            axel
            imagemagick
            unixtools.xxd
            bc
            rsync
            curl
            zip
            unzip
            wget
            exfat
            ffmpeg
            parted
            fuse2
            pkg-config
            patchelf

            psbbn
          ];

          shellHook = ''
            ${pkgs.patchelf}/bin/patchelf --set-rpath "${pkgs.fuse2.out}/lib" "./scripts/helper/PFS Fuse.elf"
            mkdir -p scripts/venv/
            ln -sfn ${pythonEnv}/* ./scripts/venv/

            echo -e "\033[1;32m==============================================================\033[0m"
            echo -e "\033[1;36m                PSBBN Definitive English Patch                \033[0m"
            echo -e "\033[1;32m==============================================================\033[0m"
            echo ""
            echo -e "Open main menu by executing: \033[1;36mpsbbn\033[0m"
            echo ""
          '';
        };

        apps = {
          psbbn = flake-utils.lib.mkApp { drv = psbbn; };
        };
      }
    );
}
