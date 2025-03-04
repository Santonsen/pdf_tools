#!/usr/bin/env python3

name = '/home/pentest/jottacloud/move_to_noter/602_mahalageasca_reidGilje/602_mahalageasca_reidGilje_cornets.pdf'

base_name, suffix_name = name.rsplit('_',1)
suffix_name = suffix_name.split('.')[0]

new_name = '_'.join([base_name,suffix_name,'split.pdf'])

print(new_name)
