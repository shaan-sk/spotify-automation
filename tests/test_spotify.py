from utils.driver_factory import create_driver
from pages.spotify_page import SpotifyPage

def test_spotify_workflow():
    driver = create_driver()
    spotify = SpotifyPage(driver)
    
    try:
        spotify.open_app()
        spotify.search_song("All The Stars")
        spotify.control_playback()
        spotify.add_to_playlist("My Fav")
        spotify.finalize()
    finally:
        driver.quit()
