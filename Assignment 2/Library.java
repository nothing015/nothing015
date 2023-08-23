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
	public void download(AudioContent content)
	{
		String theType = content.getType(); // checking the type of 'content'


		if (theType.equals("SONG")){
			for (Song song: songs){
				if (song.equals(content)){
					throw new InvalidDownloadException("Song " + song.getTitle() + " already downloaded");
				}
			}
			Song newContent = (Song) content;
			songs.add(newContent); // checks if the song is already downloaded, if not, then it is added to the library
		}
		else if (theType.equals("AUDIOBOOK")){
			for (AudioBook audiobook: audiobooks){
				if (audiobook.equals(content)){
					errorMsg = "AudioBook " + audiobook.getTitle() + " already downloaded";
					throw new InvalidDownloadException("AudioBook " + audiobook.getTitle() + " already downloaded");
				}
			}
			AudioBook newContent = (AudioBook) content;
			audiobooks.add(newContent); // repetition of the algorithm above
		}
		else if (theType.equals("PODCAST")){
			for (Podcast podcast: podcasts){
				if (podcast.equals(content)){
					errorMsg = "Podcast already downloaded";
					throw new InvalidDownloadException("Podcast already downloaded");
				}
			}
			Podcast newContent = (Podcast) content;
			podcasts.add(newContent);
		}
		else {throw new InvalidDownloadException(("Content Not Found in Store"));}

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
	public void deleteSong(int index)
	{
		if (index < 1 || index > songs.size())
		{
			throw new AudioContentNotFoundException("Song Not Found");
		}
		// searching the song in the playlists
		boolean flag = false;
		for (int i = 0; i < playlists.size(); i++)
		{
			ArrayList<AudioContent> playlist = playlists.get(i).getContent();
			playlist.remove(songs.get(index-1));
		}

		songs.remove(index-1);
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
	public void playSong(int index)
	{
		if (index < 1 || index > songs.size())
		{
			throw new AudioContentNotFoundException("Song Not Found");
		}
		songs.get(index-1).play();
	}
	
	// Play podcast from list (specify season and episode)
	// Bonus
	public void playPodcast(int index, int season, int episode)
	{
		if (index < 1 || index > podcasts.size())
		{
			throw new AudioContentNotFoundException("Podcast Not Found");
		}
		Podcast podcast = podcasts.get(index-1);
		podcast.selectSeasonAndEpisode(season, episode);
		podcast.play();
	}
	
	// Print the episode titles of a specified season
	// Bonus 
	public void printPodcastEpisodes(int index, int season)
	{
		if (index < 1 || index > podcasts.size())
		{
			throw new AudioContentNotFoundException("Podcast Not Found");
		}
		Podcast podcast = podcasts.get(index-1);
		podcast.selectSeasonAndEpisode(season, 0);
		podcast.printSeasonEpisodes();
	}
	
	// Play a chapter of an audio book from list of audiobooks
	public void playAudioBook(int index, int chapter)
	{
		if (index < 1 || index > audiobooks.size())
		{
			throw new AudioContentNotFoundException("AudioBook Not Found");
		}
		AudioBook audiobook = audiobooks.get(index-1);
		audiobook.selectChapter(chapter);
		audiobook.play();
	}
	
	// Print the chapter titles (Table Of Contents) of an audiobook
	// see class AudioBook
	public void printAudioBookTOC(int index)
	{
		if (index < 1 || index > audiobooks.size())
		{
			errorMsg = "AudioBook Not Found";
			throw new AudioContentNotFoundException("AudioBook Not Found");
		}
		audiobooks.get(index-1).printTOC();
	}
	
  /*
   * Playlist Related Methods
   */
	
	// Make a new playlist and add to playlists array list
	// Make sure a playlist with the same title doesn't already exist
	public void makePlaylist(String title)
	{

		Playlist newPlaylist = new Playlist(title);
		for (Playlist playlist: playlists)
		{
			if (playlist.equals(newPlaylist))
			{
				throw new AlreadyExistsException("Playlist " + title + " Already Exists");
			}
		}
		playlists.add(newPlaylist);
	}
	
	// Print list of content information (songs, audiobooks etc) in playlist named title from list of playlists
	public void printPlaylist(String title)
	{
		boolean flag = false;
		for (Playlist playlist: playlists)
		{
			if (playlist.getTitle().equals(title))
			{
				playlist.printContents();
				System.out.println();
				flag = true;
			}
		}
		if (flag == false) {throw new AudioContentNotFoundException("Playlist not found");}
	}
	
	// Play all content in a playlist
	public void playPlaylist(String playlistTitle)
	{
		boolean flag = false;
		for (Playlist playlist: playlists)
		{
			if (playlist.getTitle().equals(playlistTitle))
			{
				playlist.playAll();
				System.out.println();
				flag = true;
			}
		}
		if (flag == false) {throw new AudioContentNotFoundException("Playlist not found");}
	}
	
	// Play a specific song/audiobook in a playlist
	public void playPlaylist(String playlistTitle, int indexInPL)
	{
		boolean found = false;
		System.out.println(playlistTitle);
		for (Playlist playlist: playlists)
		{
			// getting the content from within the playbook
			if (playlist.getTitle().equals(playlistTitle))
			{
				found = true;
				if (indexInPL < 1 || indexInPL > playlist.getContent().size())
				{
					errorMsg = "Audio content Not Found";
					throw new AudioContentNotFoundException("Audio content Not found");
				}
				else {
					playlist.play(indexInPL-1);
				}
			}
		}
		if (found == false) {throw new AudioContentNotFoundException("Playlist not found");}
	}
	
	// Add a song/audiobook/podcast from library lists at top to a playlist
	// Use the type parameter and compare to Song.TYPENAME etc
	// to determine which array list it comes from then use the given index
	// for that list
	public void addContentToPlaylist(String type, int index, String playlistTitle)
	{
		boolean flag = false;
		for (int i = 0; i < playlists.size();i++)
		{
			Playlist playlist = playlists.get(i);
			// getting the content from within the playbook
			if (playlist.getTitle().equals(playlistTitle))
			{
				flag = true;

				if (!(type.toUpperCase().equals("SONG")||type.toUpperCase().equals("AUDIOBOOK")||type.toUpperCase().equals("PODCAST"))){
					throw new InvalidTypeException("Invalid type ");
				}
				if (type.toUpperCase().equals("SONG")&&(index >= 1 || index <= songs.size())) {
					playlist.addContent(songs.get(index-1));

				}
				else if (type.toUpperCase().equals("AUDIOBOOK")&&(index >= 1 || index <= audiobooks.size())) {
					playlist.addContent(audiobooks.get(index-1));
				}
				else if (type.toUpperCase().equals("PODCAST")&&(index >= 1 || index <= podcasts.size())) {
					playlist.addContent(podcasts.get(index-1));
				}
				else {
					throw new InvalidTypeException("Invalid audio-content ");
				}
			}
		}
		if (flag==false){throw new AudioContentNotFoundException("Playlist Not Found");}
	}

  // Delete a song/audiobook/podcast from a playlist with the given title
	// Make sure the given index of the song/audiobook/podcast in the playlist is valid 
	public void delContentFromPlaylist(int index, String title)
	{
		boolean flag = false;
		for (Playlist playlist: playlists)
		{
			// getting the content from within the playbook
			if (playlist.getTitle().equals(title))
			{
				flag = true;
				if (index < 1 || index > playlist.getContent().size())
				{
					if (flag == false) {throw new AudioContentNotFoundException("Audio content not found");}
				}
				else {
					playlist.deleteContent(index);
				}
			}
		}
		errorMsg = "Playlist not found";
		if (flag == false) {throw new AudioContentNotFoundException("Playlist not found");}
	}
}

class AudioContentNotFoundException extends RuntimeException
{
	public AudioContentNotFoundException() {}
	public AudioContentNotFoundException(String message)
	{
		super(message);
	}
}

class InvalidDownloadException extends RuntimeException
{
	public InvalidDownloadException() {}
	public InvalidDownloadException(String message)
	{
		super(message);
	}
}
class AlreadyExistsException extends RuntimeException
{
	public AlreadyExistsException() {}
	public AlreadyExistsException(String message)
	{
		super(message);
	}
}
class InvalidTypeException extends RuntimeException
{
	public InvalidTypeException() {}
	public InvalidTypeException(String message)
	{
		super(message);
	}
}