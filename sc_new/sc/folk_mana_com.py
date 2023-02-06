from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Command to run web scrapper for Flokk store"

    def handle(self, *args, **kwargs):
        from path.to.scrapper import scraping_bot, load_data_to_database
        
        scraping_bot(url, "store.flokk.com")
        load_data_to_database(1)
        self.stdout.write(self.style.SUCCESS("Scraping completed successfully"))