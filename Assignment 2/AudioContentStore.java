// Name : Mohammad Nuaiman Hasan
// ID: 501151286

import java.util.*;
import java.lang.*;
import java.io.FileNotFoundException;
import java.io.File;

// Simulation of audio content in an online store
// The songs, podcasts, audiobooks listed here can be "downloaded" to your library

public class AudioContentStore
{
		private ArrayList<AudioContent> contents;

		private Map<String, Integer> titleMap;
		private Map<String, ArrayList<Integer> > artistMap;
		private Map<String, ArrayList<Integer> > genreMap;
		public AudioContentStore()
		{
			contents = new ArrayList<AudioContent>();
			titleMap = new HashMap<String, Integer>();

			artistMap = new HashMap<String, ArrayList<Integer> >();

			genreMap = new HashMap<String, ArrayList<Integer> >();

			try {
				File filename = new File("store.txt");
				Scanner in = new Scanner(filename);
				while (in.hasNextLine()) {
					String line = in.nextLine();


					// Code to input a song's information from a file
					if (line.equals("SONG")) {
						System.out.println("Loading SONG");
						System.out.println();
						String id = in.nextLine();
						String title = in.nextLine();
						String yearString = in.nextLine();
						int year = Integer.parseInt(yearString);
						int length = Integer.parseInt(in.nextLine());
						String artist = in.nextLine();
						String composer = in.nextLine();
						String genreString = in.nextLine();
						Song.Genre genre = Song.Genre.POP;
						if (genreString.equals("POP")) {
							genre = Song.Genre.POP;
						} else if (genreString.equals("ROCK")) {
							genre = Song.Genre.ROCK;
						} else if (genreString.equals("JAZZ")) {
							genre = Song.Genre.JAZZ;
						} else if (genreString.equals("HIPHOP")) {
							genre = Song.Genre.HIPHOP;
						} else if (genreString.equals("RAP")) {
							genre = Song.Genre.RAP;
						} else if (genreString.equals("CLASSICAL")) {
							genre = Song.Genre.CLASSICAL;
						}
						int numOfLines = Integer.parseInt(in.nextLine());
						String audioFile = "";
						for (int i = 0; i < numOfLines; i++) {
							audioFile += in.nextLine();
							if (i != numOfLines - 1) {
								audioFile += "\r\n";
							}
						}
						// Inserting the song in store
						Song song = new Song(title, year, id, "SONG", audioFile, length, artist, composer, genre, audioFile);
						contents.add(song);

						int index = contents.size();

						// Updating the maps
						titleMap.put(title, index);

						if (artistMap.containsKey(artist)) {
							ArrayList<Integer> songArtists = artistMap.get(artist);
							songArtists.add(index);
							artistMap.put(artist, songArtists);
						} else {
							ArrayList<Integer> songArtists = new ArrayList<Integer>();
							songArtists.add(index);
							artistMap.put(artist, songArtists);
						}

						if (genreMap.containsKey(genreString)) {
							ArrayList<Integer> songGenres = genreMap.get(genreString);
							songGenres.add(index);
							genreMap.put(genreString, songGenres);
						} else {
							ArrayList<Integer> songGenres = new ArrayList<Integer>();
							songGenres.add(index);
							genreMap.put(genreString, songGenres);
						}
					}


					//Code to input an audiobook's information from a file
					else if (line.equals("AUDIOBOOK")) {
						System.out.println("Loading AUDIOBOOK");
						System.out.println();
						String id = in.nextLine();
						String title = in.nextLine();
						String yearString = in.nextLine();
						int year = Integer.parseInt(yearString);
						int length = Integer.parseInt(in.nextLine());
						String author = in.nextLine();
						String narrator = in.nextLine();
						int numOfChaptersTitles = Integer.parseInt(in.nextLine());
						ArrayList<String> chapterTitles = new ArrayList<String>();
						for (int i = 0; i < numOfChaptersTitles; i++) {
							chapterTitles.add(in.nextLine());
						}
						int numOfChapters = Integer.parseInt(in.nextLine());
						ArrayList<String> chapters = new ArrayList<String>();
						for (int i = 0; i < numOfChapters; i++) {
							String toAdd = in.nextLine();
							if (i != numOfChapters - 1) {
								toAdd += "\r\n";
							}
							chapters.add(toAdd);
						}

						// Inserting the audiobook in the store
						AudioBook audiobook = new AudioBook(title, year, id, "AUDIOBOOK", "", length, author, narrator, chapterTitles, chapters);
						contents.add(audiobook);

						// Updating the maps
						int index = contents.size();

						titleMap.put(title, index);

						if (artistMap.containsKey(author)) {
							ArrayList<Integer> bookAuthors = artistMap.get(author);
							bookAuthors.add(index);
							artistMap.put(author, bookAuthors);
						} else {
							ArrayList<Integer> bookAuthors = new ArrayList<Integer>();
							bookAuthors.add(index);
							artistMap.put(author, bookAuthors);
						}
					}
				}
			}
			catch (FileNotFoundException e)
			{
				System.out.println("The file \"store.txt\" does not exit");
				System.exit(1);
			}

		}

		public AudioContent getContent(int index)
		{
			if (index < 1 || index > contents.size())
			{
				return null;
			}
			return contents.get(index-1);
		}

		public void listAll()
		{
			for (int i = 0; i < contents.size(); i++)
			{
				int index = i + 1;
				System.out.print("" + index + ". ");
				contents.get(i).printInfo();
				System.out.println();
			}
		}

		public void search(String title)
		{
			boolean found = false;
			for (String key: titleMap.keySet())
			{
				if (key.equals(title))
				{
					found = true;
					System.out.print(titleMap.get(key) + ". ");
					contents.get(titleMap.get(key)-1).printInfo();
				}
			}
			if (found == false)
			{
				System.out.println("No matches for " + title);
			}
		}

		public void searchbyArtist(String artist)
		{
			boolean found = false;
			for (String key: artistMap.keySet())
			{
				if (key.equals(artist))
				{
					found = true;
					for (Integer index: artistMap.get(key))
					{
						System.out.print(index + ". ");
						contents.get(index-1).printInfo();
						System.out.println();
					}
				}
			}
			if (found == false)
			{
				System.out.println("No matches for " + artist);
			}
		}

		public void searchByGenre(String genre)
		{
			boolean found = false;
			for (String key: genreMap.keySet())
			{
				if (key.equals(genre))
				{
					found = true;
					for (int i = 0; i < genreMap.get(key).size(); i++){
						System.out.print(genreMap.get(key).get(i) + ". ");
						contents.get(genreMap.get(key).get(i)-1).printInfo();
						System.out.println();
					}
				}
			}
			if (found == false)
			{
				System.out.println("No matches for " + genre);
			}
		}

		public ArrayList<AudioContent> getArtistContent(String artist)
		{
			ArrayList<AudioContent> artistContent = new ArrayList<AudioContent>();
			for (String key: artistMap.keySet())
			{
				if (key.equals(artist))
				{
					for (Integer index: artistMap.get(key))
					{
						artistContent.add(contents.get(index-1));
					}
					break;
				}
			}
			if (artistContent.isEmpty())
			{
				System.out.println("No matches for " + artist);
			}
			return artistContent;
		}

		public ArrayList<AudioContent> getGenreContent(String genre)
		{
			ArrayList<AudioContent> genreContent = new ArrayList<AudioContent>();
			for (String key: genreMap.keySet())
			{
				if (key.equals(genre))
				{
					for (Integer index: genreMap.get(key))
					{
						genreContent.add(contents.get(index-1));
					}
					break;
				}
			}
			if (genreContent.isEmpty())
			{
				System.out.println("No matches for " + genre);
			}
			return genreContent;
		}

		// BONUS
	    public void searchPartially(String target)
		{
			{
				boolean found = false;
				for (String key: titleMap.keySet())
				{
					AudioContent content = contents.get(titleMap.get(key)-1);
					String contentString = content.getAudioFile() + Integer.toString(content.getLength()) + content.getTitle()
						+ Integer.toString(content.getYear()) + content.getId();
					if (content.getType().equals("SONG"))
					{
						Song song = (Song) content;
						contentString += song.getComposer() + song.getArtist();
						if (song.getGenre() == Song.Genre.POP) {contentString += "POP";}
						else if (song.getGenre() == Song.Genre.ROCK) {contentString += "ROCK";}
						else if (song.getGenre() == Song.Genre.JAZZ) {contentString += "JAZZ";}
						else if (song.getGenre() == Song.Genre.HIPHOP) {contentString += "HIPHOP";}
						else if (song.getGenre() == Song.Genre.RAP) {contentString += "RAP";}
						else if (song.getGenre() == Song.Genre.CLASSICAL) {contentString += "CLASSICAL";}
					}
					else if (content.getType().equals("AUDIOBOOK"))
					{
						AudioBook audiobook = (AudioBook) content;
						contentString += audiobook.getAuthor() + audiobook.getNarrator();
						for (String chapterTitle: audiobook.getChapterTitles())
						{
							contentString += chapterTitle;
						}
						for (String chapter: audiobook.getChapters())
						{
							contentString += chapter;
						}
					}

					if (contentString.contains(target))
					{
						found = true;
						System.out.print(titleMap.get(key) + ". ");
						contents.get(titleMap.get(key)-1).printInfo();
					}
				}
				if (found == false)
				{
					System.out.println("No matches for " + target);
				}
			}
		}
}