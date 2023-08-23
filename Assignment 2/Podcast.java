// Name : Mohammad Nuaiman Hasan
// ID: 501151286

import java.util.ArrayList;

public class Podcast extends AudioContent
{
    public static final String TYPENAME =	"PODCAST";
    private String host; 		// Can be multiple names separated by commas
    private ArrayList<Season> seasons;
    private int currentSeason = 0;
    private  int currentEpisode = 0;

    public Podcast(String title, int year, String id, String type, String audioFile, int length)
    {

        super(title, year, id, type, audioFile, length);
        this.host = "";
        this.seasons = new ArrayList<Season>();
    }

    public String getType()
    {
        return TYPENAME;
    }

    public void printInfo()
    {
        super.printInfo();
        System.out.println("Host: " + this.host);
        System.out.println("Seasons: " + seasons.size());
    }

    public void play()
    {
        Season season = seasons.get(currentSeason);
        super.setAudioFile(season.episodeTitles.get(currentEpisode) + "\n" + season.episodeFiles.get(currentEpisode));
        super.play();
    }

    public String getHost()
    {
        return this.host;
    }
    public void setHost(String host)
    {
        this.host = host;
    }

    // Selecting current season and current episode
    public void selectSeasonAndEpisode(int season, int episode)
    {
        if (season >= 1 && season <= seasons.size())
        {
            currentSeason = season - 1;
            if (episode >= 1 && episode <= seasons.get(currentSeason).episodeFiles.size())
            {
                currentEpisode = episode - 1;
            }
        }
    }

    // Printing all the episode titles of the current Season
    public void printSeasonEpisodes(){ // returns all episodes of the 'Current Season'
        Season season = this.seasons.get(currentSeason);
        int count = 1;
        for (String title: season.episodeTitles)
        {
            System.out.print("Episode "+ count +". ");
            System.out.println(title);
            System.out.println();
            count++;
        }
    }

    // Two podcasts are equal if their AudioContent information is equal and both the host and seasons are the same
    // Make use of the superclass equals() method
    public boolean equals(Object other)
    {
        Podcast other2 = (Podcast) other;
        return super.equals(other2) && (this.host.equals(other2.host)) && (this.seasons.equals(other2.seasons));
    }

    // Setting seasons
    public void makeSeasons(ArrayList<Season> seasonsToAdd)
    {
        this.seasons = seasonsToAdd;
    }
}