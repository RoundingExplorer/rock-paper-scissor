import java.util.*;
public class Main {
  public static void main(String[] args) {
    String something = player_move();
    com_move(something);
  }
  public static String player_move() {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Choose rock, papers, or scissors: ");
    String option = keyboard.nextLine();
    return option;
  }
  public static void com_move(String option) {
    if (option.equals("rock")) {
      String[]rock = {"Paper", "Scissors"};
      int comchoice1 = new Random().nextInt(rock.length);  
      String rock1 = (rock [comchoice1]);
      System.out.println("Computer chooses: " + rock1);
      if (rock1.equals("Scissors")) {
        System.out.println("You win!");
      }
      else {
        System.out.println("Computer wins!");
      }
    }
    else if (option.equals("paper")) {
      String[]paper = {"Rock", "Scissors"};
      int comchoice2 = new Random().nextInt(paper.length);
      String paper1 = (paper [comchoice2]);
      System.out.println("Computer chooses: " + paper1);
      if (paper1.equals("Rock")) {
        System.out.println("You win!");
      }
      else {
        System.out.println("Computer wins!");
      }
    }
    else if (option.equals("scissors")) {
      String[]scissors = {"Rock", "Paper"};
      int comchoice3 = new Random().nextInt(scissors.length);
      String scissors1 = (scissors [comchoice3]);
      System.out.println("Computer chooses: " + scissors1);
      if (scissors1.equals("Paper")) {
        System.out.println("You win!");
      }
      else {
        System.out.println("Computer wins!");
      }
    }
  }
}
