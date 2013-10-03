"""
Usage:
    node-cleaner.py <server> <user> <key-file> [--debug]

Options:
    --debug          include more detailed output
"""

import boto
import boto.exception

from docopt import docopt

import chef


def clean(chef_server, chef_user, chef_key, debug=False):
    ec2 = boto.connect_ec2()
    with chef.ChefAPI(chef_server, chef_key, chef_user):
        for node_name in chef.Node.list():
            node = chef.Node(node_name)
            if node.has_key('ec2') and 'instance_id' in node['ec2']:
                try:
                    instance_id = node['ec2']['instance_id']
                    instances = ec2.get_all_instances([instance_id])
                    instance = instances[0].instances[0]
                    if debug:
                        print instance, instance.state
                    state = instance.state
                    if state == 'terminated' or state == 'stopped':
                        if debug:
                            print "Removing non-existent node: {0}".format(
                                node.name
                            )
                        node.delete()
                        client = chef.Client(node.name)
                        client.delete()
                except boto.exception.EC2ResponseError:
                    if debug:
                        print "Removing non-existent node: {0}".format(
                            node.name
                        )
                    node.delete()
                    client = chef.Client(node.name)
                    client.delete()
                except IndexError:
                    if debug:
                        print "Removing non-existent node: {0}".format(
                            node.name
                        )
                    node.delete()
                    client = chef.Client(node.name)
                    client.delete()


def main():
    arguments = docopt(__doc__, version='Node Cleaner 1.0')
    clean(arguments['<server>'], arguments['<user>'], arguments['<key-file>'],
          arguments['--debug'])


if __name__ == '__main__':
    main()
