import click
import pdpyras
import json

@click.command()
@click.argument("routing_key")
@click.argument("dedup_key")
@click.argument("summary")
@click.argument("source")
@click.argument("custom_details", required=False)
def main(routing_key, dedup_key, summary, source, custom_details=None):
    print("Staring event API call")
    if custom_details is not None:
        details = json.loads(custom_details)

    print(f"{dedup_key}: {summary} {source} {custom_details}")

    session = pdpyras.EventsAPISession(routing_key)
    session.trigger(summary, source, dedup_key=dedup_key, custom_details=details)

if __name__ == '__main__':
    main()
