from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Runs the web scraper to extract data from the website and save it to the database."

    def handle(self, *args, **kwargs):
        from .scrap import scraping_bot, load_data_to_database
        
        scraping_bot()
        load_data_to_database()
        self.stdout.write(self.style.SUCCESS("Web scraping completed successfully!"))