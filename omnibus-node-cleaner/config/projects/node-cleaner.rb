name "node-cleaner"
maintainer "Tom Howe"
homepage "CHANGEME.com"

replaces        "node-cleaner"
install_path    "/opt/node-cleaner"
build_version   "1.0.0"
build_iteration 5

# creates required build directories
dependency "preparation"
dependency "node-cleaner"
dependency "version-manifest"


# version manifest file

exclude "\.git*"
exclude "bundler\/git"
