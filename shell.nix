{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    pkgs.python3
    pkgs.python3Packages.kivy
    pkgs.python3Packages.pudb
    pkgs.python3Packages.selenium
  ];

}
