import org.jfugue.player.Player;
import java.io.*;
import java.util.Scanner;

public class MusicPlayer
{
	public static void main(String[] args) throws Exception
	{
		Player player = new Player();

		String audio = readFile();
		//player.play("C D E F G A B");
		player.play(audio);
	}

	public static String readFile() throws Exception
	{
		String audio = "";

		File f = new File("ByteR");
		Scanner sc = new Scanner(f);

		audio = sc.nextLine();
		//while(sc.hasNext())
		//{
		//	String line = sc.readLine();
		//	Scanncer scan = new Scanner(line).useDelimiter(" ");
		//	audio = audio + " " + scan.next();
		//}
		return audio;
	}
}
