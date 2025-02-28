import click

from ..auth.oauth import OAuthHandler
from ..clients.crm.client import CRMClient


@click.group()
def cli():
    pass


@click.command()
def auth():
    """Retrieves and displays access token."""
    click.echo(f"Access Token: {OAuthHandler.get_access_token()}")


@click.command()
def get_leads():
    """Fetches leads from Zoho CRM."""
    client = CRMClient()
    leads = client.get_leads()
    click.echo(leads)


cli.add_command(auth)
cli.add_command(get_leads)

if __name__ == "__main__":
    cli()
