import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {


  ngOnInit(): void {
  }
  
  username: string;
  password: string;
  message: string;
  showErrorMessage: boolean;

  constructor(public service_login: LoginService, public router: Router) {}


  login() {
    this.showErrorMessage = false;
    const user = {username: this.username, password: this.password};
    console.log(this.username);
    console.log(this.password);

    this.service_login.login(user).subscribe( data => {
      console.log(data);
      console.log(user.username);  
      this.service_login.setUser(user.username);  
      this.service_login.setToken(data.token);
      this.service_login.setLogin(true);
      this.service_login.getToken();
      this.router.navigateByUrl('/');
    },
    (error)=>{
      console.log(error);
      this.message="Usuario o contraseña incorrecta";
      console.log("error");
      this.showErrorMessage = true;

    }    
    );
  }
}
