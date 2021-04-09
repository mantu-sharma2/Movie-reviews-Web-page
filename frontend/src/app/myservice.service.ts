import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class MyserviceService {
    private finaldata = [];
    private apiurl = 'http://localhost:8000';

    constructor (private http: HttpClient) {}

    getMoviesList() {
        return this.http.get(this.apiurl);
    }

    getMovieDetails(id: number) {
        return this.http.get(this.apiurl + '/details/'+id);
    }

    upvoteMovie(id: number) {
        return this.http.get(this.apiurl + '/upvote/'+id)
    }
}