let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable";
  pkgs = import nixpkgs {};

  # nixpkgs/e8b0430bc4c4235607ae102010dec2ba32e8c0ca#openai
  nixpkgs2 = fetchTarball "https://github.com/NixOS/nixpkgs/archive/e8b0430bc4c4235607ae102010dec2ba32e8c0ca.tar.gz";
  other."pkgs-openai-0.28.1" = import nixpkgs2 {};
in pkgs.mkShellNoCC {
  packages = with pkgs; [
    (python3.withPackages (python-pkgs: with python-pkgs; [
      python-dotenv
      requests
      termcolor
      tqdm
    ]))
    other."pkgs-openai-0.28.1".python310Packages.openai
  ];
}
