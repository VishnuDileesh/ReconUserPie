from pyfiglet import Figlet
import click
import requests
from platforms_list import platforms

f = Figlet(
        font='slant',
        width=80
        )

__author__ = "vishnu_dileesh"

click.echo(click.style(f.renderText('ReconUserPie'), bold=True, fg='cyan'))
print('Author : ' + __author__)
print('Message : Do No Evil \n \n')





@click.command()

#@click.option('--username', prompt=True)

@click.option('--flag', '-f', help='Set flags to choose the search results')

def main(flag):
    """
    Tool Outputs 3 Types Of Results

    1) Success : Username is successfully found on the platform

    2) Failure : Username is not found on the platform

    3) Doubtful : Tool is not confident about the result, please do manual check



    python3 reconuser.py (Does all platforms search & outputs all the above result types)

    python3 -f ms reconuser.py (Does platforms searches excluding Doubtful cases)

    python3 -f ss reconuser.py (Does platforms searches excluding Doubtful cases & outputs only Success results)


    """

    click.echo("Python OSINT Recon Script/Tool For Enumerating Online Presence Of A Person From Username \n")
    click.echo("Enumerates 73 Online Platforms \n\n")


    if flag == 'ms':

        click.echo("ReconUserPie running with flag min-search (excludes doubtful platforms) \n\n")

    elif flag == 'ss':

        click.echo("ReconUserPie running with flag success-search (excludes doubtful platforms & shows only Success results \n\n")

    username = click.prompt("Username")


    click.echo("\n\n")

    rU = reconUser(username, flag)



class reconUser():
    def __init__(self, username, flag):



        for k, v in platforms.items():

            if flag == 'ms':

                if v['doubt'] == True:

                    continue

                else:

                    if v['up']:

                        click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                        site = 'https://' + username + v['url']

                        enumsearch(site, k, v, username, flag)

                    else:

                        click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                        site = v['url'] + username

                        enumsearch(site, k, v, username, flag)

            elif flag == 'ss':

                if v['doubt'] == True:

                    continue

                else:

                    if v['up']:

                        click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                        site = 'https://' + username + v['url']

                        enumsearch(site, k, v, username, flag)

                    else:

                        click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                        site = v['url'] + username

                        enumsearch(site, k, v, username, flag)


            else:

                if v['up']:

                    click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                    site = 'https://' + username + v['url']

                    enumsearch(site, k, v, username, flag)

                else:

                    click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                    site = v['url'] + username

                    enumsearch(site, k, v, username, flag)



def enumsearch(site, k, v, username, flag):
    try:

        r = requests.get(site)


        if r.status_code == 200:

            if v['doubt'] == True:

                click.echo(click.style((f"Doubtful: {username} Found in {k}"), bold=True, fg='black'))

                click.echo(click.style((f'{site}'), fg='white', bold=False))

            else:

                click.echo(click.style((f"Success:{username} Found in {k}"), blink=True, bold=True, fg='white', bg='blue'))

                click.echo(click.style((f"{site}"), fg='white', bg='yellow', bold=True))


        else:

            if v['doubt'] == True:

                click.echo(click.style((f"Failure:{username} Not Found in {k}"), bold=True, fg='black'))

            else:

                click.echo(click.style((f"Failure:{username} Not Found in {k}"), bold=True, fg='white', bg='red'))

    except:

        click.echo(click.style((f"Error: {site}"), blink=True, bold=True, fg='red', bg='white'))






if __name__ == "__main__":
    main()
