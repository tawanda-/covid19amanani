import click
from . import api_wrapper
from . import api_dao

'''
    Get Data for Africa, either 
        1. the latest infections, deaths data,
        2. vaccination data and
        3. historical infections and deaths data.

    To run the commannd, in command line type: flask get-data -t [latest/vaccine/history] -s [confirmed/deaths]
    --type is required and the options are : latest, vaccine, history
    If user selects history then status is required. For latest and vaccine status is not required
    
'''

@click.command('get-data')
@click.option('-t', '--type', required=True, help='Choices: latest, vaccine, history')
@click.option('-s', '--status', help='either confirmed or deaths')
def get_data_command(type, status):

    parameters = {'continent':'africa'}
    response = {}

    if type and type in ['latest','vaccine']:
        response = api_wrapper.get(type, parameters)
    elif type and type == 'history':
        if status in ['confirmed', 'deaths']:
            parameters.update({'status':status})
            response = api_wrapper.get(type, parameters)
        else:
            click.echo('--status is required, options [confirmed/deaths]')
            return
    else:
        click.echo(f'--type is required, options: [latest/vaccine/history]')
        return

    if response:
        api_dao.insert(type, response)
        click.echo(f'Succesfully added {type} data.')
    else:
        click.echo(f'Oops something wennt wrong please try again.')