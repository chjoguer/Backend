import { Routes, RouterModule } from '@angular/router';

import { HeaderComponent } from './common/header/header.component';
import { FooterComponent } from './common/footer/footer.component';
import { IndexComponent } from './components/index/index.component';
import { GalleryComponent } from './components/gallery/gallery.component';
import {LoginComponent } from './components/login/login.component';

const routes: Routes = [
    { path: '', component: IndexComponent },
    { path: 'galeria', component: GalleryComponent },
    { path: 'login', component: LoginComponent},

   // { path: 'login', component: HeaderComponent },
    //{ path: 'register', component: RegisterComponent },

    // otherwise redirect to home
];

export const appRoutingModule = RouterModule.forRoot(routes);