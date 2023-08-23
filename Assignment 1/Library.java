// Name : Mohammad Nuaiman Hasan
// ID: 501151286

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/*
 * This class manages, stores, and plays audio content such as songs, podcasts and audiobooks. 
 */
public class Library
{
	private ArrayList<Song> 			songs; 
	private ArrayList<AudioBook> 	audiobooks;
	private ArrayList<Playlist> 	playlists; 
	
	private ArrayList<Podcast> 	podcasts;
	
	// Public methods in this class set errorMesg string 
	// Error Messages can be retrieved from main in class MyAudioUI by calling  getErrorMessage()
	// In assignment 2 we will replace this with Java Exceptions
	String errorMsg = "";
	
	public String getErrorMessage()
	{
		return errorMsg;
	}

	public Library()
	{
		songs 			= new ArrayList<Song>(); 
		audiobooks 	= new ArrayList<AudioBook>(); ;
		playlists   = new ArrayList<Playlist>();
		podcasts		= new ArrayList<Podcast>(); ;
	}
	/*
	 * Download audio content from the store. Since we have decided (design decision) to keep 3 separate lists in our library
	 * to store our songs, podcasts and audiobooks (we could have used one list) then we need to look at the type of
	 * audio content (hint: use the getType() method and compare to Song.TYPENAME or AudioBook.TYPENAME etc)
	 * to determine which list it belongs to above
	 * 
	 * Make sure you do not add song/podcast/audiobook to a list if it is already there. Hint: use the equals() method
	 * If it is already in a list, set the errorMsg string and return false. Otherwise add it to the list and return true
	 * See the video
	 */
	public boolean download(AudioContent content)
	{
		String theType = content.getType(); // checking the type of 'content'

		if (theType.equals("SONG")){
			for (Song song: songs){
				if (song.equals(content)){
					errorMsg = "Song already downloaded";
					return false;
				}
			}
			Song newContent = (Song) content;
			songs.add(newContent); // checks if the song is already downloaded, if not, then it is added to the library
			return true;
		}
		else if (theType.equals("AUDIOBOOK")){
			for (AudioBook audiobook: audiobooks){
				if (audiobook.equals(content)){
					errorMsg = "AudioBook already downloaded";
					return false;
				}
			}
			AudioBook newContent = (AudioBook) content;
			audiobooks.add(newContent); // repetition of the algorithm above
			return true;
		}
		else if (theType.equals("PODCAST")){
			for (Podcast podcast: podcasts){
				if (podcast.equals(content)){
					errorMsg = "Podcast already downloaded";
					return false;
				}
			}
			Podcast newContent = (Podcast) content;
			podcasts.add(newContent);
			return true;
		}
		return false;
	}
	
	// Print Information (printInfo()) about all songs in the array list
	public void listAllSongs()
	{
		for (int i = 0; i < songs.size(); i++)
		{
			int index = i + 1;
			System.out.print("" + index + ". ");
			songs.get(i).printInfo();
			System.out.println();	
		}
	}
	
	// Print Information (printInfo()) about all audiobooks in the array list
	public void listAllAudioBooks()
	{
		for (int i = 0; i < audiobooks.size(); i++)
		{
			int index = i + 1;
			System.out.print("" + index + ". ");
			audiobooks.get(i).printInfo();
			System.out.println();
		}
	}
	
  // Print Information (printInfo()) about all podcasts in the array list
	public void listAllPodcasts()
	{
		for (int i = 0; i < podcasts.size(); i++)
		{
			int index = i + 1;
			System.out.print("" + index + ". ");
			podcasts.get(i).printInfo();
			System.out.println();
		}
	}
	
  // Print the name of all playlists in the playlists array list
	// First print the index number as in listAllSongs() above
	public void listAllPlaylists()
	{
		for (int i = 0; i < playlists.size(); i++)
		{
			int index = i + 1;
			System.out.print("" + index + ". ");
			System.out.println(playlists.get(i).getTitle());
			System.out.println();
		}
	}
	
  // Print the name of all artists. 
	public void listAllArtists()
	{
		// First create a new (empty) array list of string 
		// Go through the songs array list and add the artist name to the new arraylist only if it is
		// not already there. Once the artist array list is complete, print the artists names
		ArrayList<String> newList = new ArrayList<String>();

		for (Song song: songs){
			if (!(newList.contains(song.getArtist()))){
				newList.add(song.getArtist());
			}
		}
		for (int i = 0; i < newList.size(); i++)
		{
			int index = i + 1;
			System.out.print("" + index + ". ");
			System.out.println(newList.get(i));
			System.out.println();
		}
		
	}

	// Delete a song from the library (i.e. the songs list) - 
	// also go through all playlists and remove it from any playlist as well if it is part of the playlist
	public boolean deleteSong(int index)
	{
		if (index < 1 || index > songs.size())
		{
			errorMsg = "Song Not Found";
			return false;
		}
		// searching the song in the playlists
		boolean flag = false;
		for (int i = 0; i < playlists.size(); i++)
		{
			ArrayList<AudioContent> playlist = playlists.get(i).getContent();
			playlist.remove(songs.get(index-1));
		}

		songs.remove(index-1);
		return true;
	}
	
  //Sort songs in library by year
	public void sortSongsByYear()
	{
		// Use Collections.sort()
		Collections.sort(songs, new SongYearComparator()); // using the Song year comparator

	}
  // Write a class SongYearComparator that implements
	// the Comparator interface and compare two songs based on year
	private class SongYearComparator implements Comparator<Song>
	{
		public int compare(Song a, Song b){
			return a.getYear() - b.getYear();
		}
	}

	// Sort songs by length
	public void sortSongsByLength()
	{
	 // Use Collections.sort()
		Collections.sort(songs, new SongLengthComparator());
	}
  // Write a class SongLengthComparator that implements
	// the Comparator interface and compare two songs based on length
	private class SongLengthComparator implements Comparator<Song>
	{
		public int compare(Song a, Song b){
			return a.getLength() - b.getLength();
		}
	}

	// Sort songs by title 
	public void sortSongsByName()
	{
	  // Use Collections.sort()
		// class Song should implement the Comparable interface
		// see class Song code
		Collections.sort(songs);
	}

	
	
	/*
	 * Play Content
	 */
	
	// Play song from songs list
	public boolean playSong(int index)
	{
		if (index < 1 || index > songs.size())
		{
			errorMsg = "Song Not Found";
			return false;
		}
		songs.get(index-1).play();
		return true;
	}
	
	// Play podcast from list (specify season and episode)
	// Bonus
	public boolean playPodcast(int index, int season, int episode)
	{
		if (index < 1 || index > podcasts.size())
		{
			errorMsg = "Podcast Not Found";
			return false;
		}
		Podcast podcast = podcasts.get(index-1);
		podcast.selectSeasonAndEpisode(season, episode);
		podcast.play();
		return true;
	}
	
	// Print the episode titles of a specified season
	// Bonus 
	public boolean printPodcastEpisodes(int index, int season)
	{
		if (index < 1 || index > podcasts.size())
		{
			errorMsg = "Podcast Not Found";
			return false;
		}
		Podcast podcast = podcasts.get(index-1);
		podcast.selectSeasonAndEpisode(season, 0);
		podcast.printSeasonEpisodes();
		return true;
	}
	
	// Play a chapter of an audio book from list of audiobooks
	public boolean playAudioBook(int index, int chapter)
	{
		if (index < 1 || index > audiobooks.size())
		{
			errorMsg = "AudioBook Not Found";
			return false;
		}
		AudioBook audiobook = audiobooks.get(index-1);
		audiobook.selectChapter(chapter);
		audiobook.play();
		return true;
	}
	
	// Print the chapter titles (Table Of Contents) of an audiobook
	// see class AudioBook
	public boolean printAudioBookTOC(int index)
	{
		if (index < 1 || index > audiobooks.size())
		{
			errorMsg = "AudioBook Not Found";
			return false;
		}
		audiobooks.get(index-1).printTOC();
		return true;
	}
	
  /*
   * Playlist Related Methods
   */
	
	// Make a new playlist and add to playlists array list
	// Make sure a playlist with the same title doesn't already exist
	public boolean makePlaylist(String title)
	{
		Playlist newPlaylist = new Playlist(title);
		for (Playlist playlist: playlists)
		{
			if (playlist.equals(newPlaylist))
			{
				errorMsg = "Playlist " + title + " Already Exists";
				return false;
			}
		}
		playlists.add(newPlaylist);
		return true;
	}
	
	// Print list of content information (songs, audiobooks etc) in playlist named title from list of playlists
	public boolean printPlaylist(String title)
	{
		for (Playlist playlist: playlists)
		{
			if (playlist.getTitle().equals(title))
			{
				playlist.printContents();
				System.out.println();
				return true;
			}
		}
		errorMsg = "Playlist not found";
		return false;
	}
	
	// Play all content in a playlist
	public boolean playPlaylist(String playlistTitle)
	{
		for (Playlist playlist: playlists)
		{
			if (playlist.getTitle().equals(playlistTitle))
			{
				playlist.playAll();
				System.out.println();
				return true;
			}
		}
		errorMsg = "Playlist not found";
		return false;
	}
	
	// Play a specific song/audiobook in a playlist
	public boolean playPlaylist(String playlistTitle, int indexInPL)
	{
		System.out.println(playlistTitle);
		for (Playlist playlist: playlists)
		{
			// getting the content from within the playbook
			if (playlist.getTitle().equals(playlistTitle))
			{
				if (indexInPL < 1 || indexInPL > playlist.getContent().size())
				{
					errorMsg = "Audio content Not Found";
					return false;
				}
				else {
					playlist.play(indexInPL-1);
					return true;
				}
			}
		}
		errorMsg = "Playlist not found";
		return false;
	}
	
	// Add a song/audiobook/podcast from library lists at top to a playlist
	// Use the type parameter and compare to Song.TYPENAME etc
	// to determine which array list it comes from then use the given index
	// for that list
	public boolean addContentToPlaylist(String type, int index, String playlistTitle)
	{
		for (int i = 0; i < playlists.size();i++)
		{
			Playlist playlist = playlists.get(i);
			// getting the content from within the playbook
			if (playlist.getTitle().equals(playlistTitle))
			{

				if (!(type.toUpperCase().equals("SONG")||type.toUpperCase().equals("AUDIOBOOK")||type.toUpperCase().equals("PODCAST"))){
					errorMsg = "Invalid type ";
					return false;
				}
				if (type.toUpperCase().equals("SONG")&&(index >= 1 || index <= songs.size())) {
					playlist.addContent(songs.get(index-1));
					return true;
				}
				else if (type.toUpperCase().equals("AUDIOBOOK")&&(index >= 1 || index <= audiobooks.size())) {
					playlist.addContent(audiobooks.get(index-1));
					return true;
				}
				else if (type.toUpperCase().equals("PODCAST")&&(index >= 1 || index <= podcasts.size())) {
					playlist.addContent(podcasts.get(index-1));
					return true;
				}
				else {
					errorMsg = "Invalid audio-content ";
					return false;
				}
			}
		}
		errorMsg = "Playlist not found ";
		return false;
	}

  // Delete a song/audiobook/podcast from a playlist with the given title
	// Make sure the given index of the song/audiobook/podcast in the playlist is valid 
	public boolean delContentFromPlaylist(int index, String title)
	{
		for (Playlist playlist: playlists)
		{
			// getting the content from within the playbook
			if (playlist.getTitle().equals(title))
			{
				if (index < 1 || index > playlist.getContent().size())
				{
					errorMsg = "Audio content Not Found";
					return false;
				}
				else {
					playlist.deleteContent(index);
					return true;
				}
			}
		}
		errorMsg = "Playlist not found";
		return false;
	}
	
}

