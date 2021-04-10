import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
// import { monitorEventLoopDelay } from 'node:perf_hooks';
import { MyserviceService } from '../../myservice.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})

export class DetailsComponent implements OnInit {
  private id = 1;
  public movie : any;
  constructor(private myservice: MyserviceService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    this.myservice.getMovieDetails(this.id).subscribe((data) => {
      this.movie = data;
      
    })
  }
  
  public upvote()  {
    this.myservice.upvoteMovie(this.id).subscribe((data) => {
      this.movie = data;
    })
  }

  public downvote()  {
    this.myservice.downvoteMovie(this.id).subscribe((data) => {
      this.movie = data;
    })
  }
}
