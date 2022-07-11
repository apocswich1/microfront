import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PublicHomeComponent } from './public-home/public-home.component';

const routes: Routes = [
  { path: '', component: PublicHomeComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule {
}
