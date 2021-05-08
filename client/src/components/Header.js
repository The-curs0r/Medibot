import React from 'react';
import "./Header.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav} from 'react-bootstrap'
const Header = ()=>{
    return(
        <Navbar bg="dark" variant="dark" expand="lg" >
			<Navbar.Brand href="/">Medibot</Navbar.Brand>
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
				<Nav className="justify-content-end">
					<Nav.Link  className="ml-auto" href="/">Home</Nav.Link>
					<Nav.Link  className="ml-auto" href="/medibot">Bot</Nav.Link>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
    )
}


export default Header;