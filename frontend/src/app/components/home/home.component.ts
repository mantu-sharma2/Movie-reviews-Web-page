import { Component, OnInit } from '@angular/core';
import { MyserviceService } from '../../myservice.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  public movieslist: any;
  // public greet = "Hello World!!!";

  constructor(private myservice: MyserviceService) { }

  ngOnInit(): void {
    this.myservice.getMoviesList().subscribe((data) => {
      console.log(data);
      this.movieslist = data;
      // this.greet += ' I am Captain Jack Sparrow';
    })
  }

  public sortMovies(by: number) {
    if (by == 1) { // name
      console.log("Sorting by name")
      this.movieslist.movies.sort((a: any, b: any) => a.name.localeCompare(b.name));
    } else if (by == 2) { // upvote
      console.log("Sorting by Upvote")
      this.movieslist.movies.sort((a: any, b: any) => b.Upvote-a.Upvote);
    } else if (by == 3) { // date
      console.log("Sorting by Date")
      this.movieslist.movies.sort((a: any, b: any) => b.name.localeCompare(a.name));
    }
  }

}
