import { Component } from '@angular/core';
//import { DevAuthService } from '../../shared/auth/devauth.service';
import { assetUrl } from 'src/single-spa/asset-url';

@Component({
  selector: 'dvp-public-home',
  templateUrl: './public-home.component.html',
  styleUrls: ['./public-home.component.scss']
})
export class PublicHomeComponent {

  Img5 = assetUrl('/img/icono-05.png');
  Img6 = assetUrl('img/icono-06.png');
  Img7 = assetUrl('img/icono-07.png');

   timeStamp: number | undefined;

  constructor(
   // private devAuthService: DevAuthService
  ) {}
  get isLoggedIn(): boolean {
    return true;
  //  return this.devAuthService.isLoggedIn;
  }

  public refreshImg(): void {
    this.timeStamp = new Date().getTime();
  }

  getData() {
    return sessionStorage.getItem('name');
  }
  
  getSession() {
    return sessionStorage.getItem('isLoggedIn');
  }

  getLogoImg(): string {
    if (this.timeStamp) {
      return this.Img5 + '?' + this.timeStamp;
    }
    return this.Img5;
  }

  getImg2(img:string): string {
    let imagen = "";
    console.log(img);
    switch (img) {
      case 'icono-05.png':
        imagen = this.Img5
        break;
      case 'icono-06.png':
        imagen = this.Img6
        break;
      case 'icono-07.png':
        imagen = this.Img7
        break;
    
      default:
        break;
    }

    return imagen;
  }
}
