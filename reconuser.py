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

def main():
    """

    python3 reconuser.py

    """

    click.echo("Python OSINT Recon Script/Tool For Enumerating Online Presence Of A Person From Username \n")
    click.echo("Enumerates 73 Online Platforms \n\n")

    username = click.prompt("Username")

    click.echo("\n\n")

    rU = reconUser(username)






#@main.command()
#@click.argument('username')
#def main(username):
    
#    rU = reconUser(username)


class reconUser():
    def __init__(self, username):



        for k, v in platforms.items():

            if v['up']:

                click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                site = 'https://' + username + v['url']

                enumsearch(site, k, v, username)

            else:

                click.echo(click.style((f"Recon: {k}"), fg="white", bold=True))

                site = v['url'] + username

                enumsearch(site, k, v, username)



def enumsearch(site, k, v, username):
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
