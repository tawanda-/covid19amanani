import React from "react";
import logo from '../logo.svg'

function Header(props){
    return(
        <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
            <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                <img
                  src={logo}
                  className="bi me-2 d-inline-block"
                  width={40}
                  height={32}
                />
                <span class="fs-4">  Covid-19 Amanani</span>
            </a>
            <ul class="nav">
                <li><a href="/" class="nav-link px-2 link-secondary">Home</a></li>
                <li><a href="/dashboard" class="nav-link px-2 link-dark">Dashboard</a></li>
            </ul>
        </header>
    );
}

export default Header;