# This is an example software definition for a Ruby project.
#
# Lots of software definitions for popular open source software
# already exist in `opscode-omnibus`:
#
#  https://github.com/opscode/omnibus-software/tree/master/config/software
#
name "node-cleaner"
version "master"

dependency "python"
dependency "pip"

source :git => "https://github.com/turtlebender/node-cleaner.git"


relative_path "node-cleaner"

build do
  command "#{install_dir}/embedded/bin/pip install -r requirements.txt"
  command "#{install_dir}/embedded/bin/python setup.py install"
  command "test -h #{install_dir}/bin/node-cleaner || ln -s #{install_dir}/embedded/bin/node-cleaner #{install_dir}/bin/node-cleaner"
end
