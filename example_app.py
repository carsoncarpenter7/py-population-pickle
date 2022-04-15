#!/usr/bin/env python3
#
# Copyright (c) 2022, Michael Shafae
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 
#

"""Example of how to use us_state.pckl and ca_county.pckl pickle files."""

from collections import namedtuple
import pickle
import locale

State = namedtuple(
    'State',
    [
        'name',
        'area_sq_mi',
        'land_area_sq_mi',
        'water_area_sq_mi',
        'population',
        'n_rep_votes',
        'n_senate_votes',
        'n_ec_votes',
    ],
)

CACounty = namedtuple(
    'CACounty', ['name', 'county_seat', 'population', 'area_sq_mi']
)


def _str(item):
    """Handy function to return the named field name of a state or county."""
    return f'{item.name}'


State.__str__ = _str
CACounty.__str__ = _str


def main():
    """Main function"""
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    with open('ca_county.pckl', 'rb') as file_handle:
        ca_counties = pickle.load(file_handle)

    with open('us_state.pckl', 'rb') as file_handle:
        states = pickle.load(file_handle)

    states.sort(key=lambda x: x.area_sq_mi)
    print(
        f'The largest state or territory by area is {states[-1]} ' \
        f'and the smallest one is {states[0]}.'
    )

    ca_counties.sort(key=lambda x: x.area_sq_mi)
    print(
        f'The largest CA county by area is {ca_counties[-1]}'
        f' and the smallest one is {ca_counties[0]}.'
    )

    total_us_population = sum([s.population for s in states])
    print(f'The total US population is {total_us_population:n}.')
    # territories_only = [s for s in states if s.n_ec_votes == 0]
    states_only = [s for s in states if s.n_senate_votes > 0 and s.n_rep_votes > 0]
    total_states_only_population = sum([s.population for s in states_only])
    print(
        f'The total US population from states is {total_states_only_population:n}.'
    )
    print(
        'This means that there are '
        f'{total_us_population - total_states_only_population:n} people'
        ' who live in US territories.'
    )
    total_ec_votes = sum([s.n_ec_votes for s in states])
    print(f'The total number of Electoral College votes is {total_ec_votes}.')

    total_ca_population = sum([c.population for c in ca_counties])
    print(f'The total population of California is {total_ca_population:n}.')
    print(
        'California is '
        f'{(total_ca_population / total_us_population) * 100:.2f}% of '
        ' the US total population.'
    )
    ca_counties.sort(key=lambda x: x.population, reverse=True)
    n_counties = 3
    ca_population_largest_counties = sum(
        [c.population for c in ca_counties[:n_counties]]
    )
    county_names = ', '.join(map(str, ca_counties[:n_counties]))
    print(
        f'The population of the largest {n_counties} counties '
        f'({county_names}) in CA is {ca_population_largest_counties:n} '
        'which is '
        f'{(ca_population_largest_counties / total_ca_population) * 100:.2f}%'
        ' of CA total population or '
        f'{(ca_population_largest_counties / total_us_population) * 100:.2f}%'
        ' of the US population.'
    )
    
    # Given the sum of the population from the  third, fourth, and fifth 
    # most populated counties in California, how many US states have a population 
    # less than the sum of these three counties?

    # Find Sum of 3rd, 4th, and 5th most populated states
    print("\nQuiz #1: \n")
    ca_counties.sort(key=lambda x: x.area_sq_mi)
    print(
        f'The 3rd, 4th, and 5th most populated counties in CA by area is {ca_counties[-3]}, {ca_counties[-4]}, and {ca_counties[-5]}.'
    )
    
    print(
        f'The population of {ca_counties[-3]} '
        f'is {ca_counties[-3][-2]} '
    )
    kern = ca_counties[-3][-2]
    # print(kern)
    
    print(
        f'The population of {ca_counties[-4]} '
        f'is {ca_counties[-4][-2]} '
    )
    riverside = ca_counties[-4][-2]
    # print(riverside)
    
    print(
        f'The population of {ca_counties[-5]} '
        f'is {ca_counties[-5][-2]} '
    )
    you = ca_counties[-5][-2]
    # print(you)
    populated_county = kern + riverside + you
    print(f'sum = {populated_county}')
    
    
    counter = 0
    counter1 = 0
    states_only = [s for s in states if s.n_senate_votes > 0 and s.n_rep_votes > 0]
    # print (states_only)
    total_states_only_population = [s.population for s in states_only]
    print(
        f'The total US population from states is {total_states_only_population}\n.'
    )
    
    for i in total_states_only_population:
        if (i < populated_county):
            counter +=1
    print(counter)
    
    total_states_only_population.sort()
    # print(f'{total_states_only_population}')
    
    for i in total_states_only_population:
        if (i < populated_county):
            counter1 +=1
    print(f'sorted \n: {counter1}')
    
    # print(ca_counties)
    
    counter2 = 0
    ca_counties.sort(key=lambda x: x.area_sq_mi)
    # print(states_only)
    for i in states_only:
        area = i.area_sq_mi
        # print(area)
        if (area <= 20062.0):
            counter2 +=1
    print(counter2)
    
    # #1 38
    # #2 9
    # #3 47
if __name__ == '__main__':
    main()
