import React from "react";
import { Link } from "react-router-dom";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Home, Package, Truck, Menu } from "lucide-react";

const navItems = [
  { path: "/", label: "Dashboard", icon: <Home size={20} /> },
  { path: "/shipments", label: "Shipments", icon: <Package size={20} /> },
  { path: "/vehicles", label: "Vehicles", icon: <Truck size={20} /> },
];

const Sidebar = () => {
  return (
    <>
      <Sheet>
        <SheetTrigger className="p-2 fixed top-4 left-4 bg-gray-900 text-white rounded-md md:hidden">
          <Menu size={24} />
        </SheetTrigger>
        <SheetContent side="left" className="w-60 bg-gray-900 text-white p-6">
          <div className="mb-8">
            <p className="text-lg font-semibold tracking-wide uppercase text-gray-200">
              Shipments Dashboard
            </p>
          </div>
          <nav className="space-y-3">
            {navItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                className="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-800 transition-all duration-200"
              >
                {item.icon}
                <span className="text-gray-300">{item.label}</span>
              </Link>
            ))}
          </nav>
        </SheetContent>
      </Sheet>

      <div className="h-screen w-60 bg-gray-900 text-white fixed top-0 left-0 hidden md:flex flex-col p-6 border-r border-gray-800">
        <div className="mb-8">
          <p className="text-lg font-semibold tracking-wide uppercase text-gray-200">
            Shipments Dashboard
          </p>
        </div>
        <nav className="space-y-3">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-800 transition-all duration-200"
            >
              {item.icon}
              <span className="text-gray-300">{item.label}</span>
            </Link>
          ))}
        </nav>
      </div>
    </>
  );
};

export default Sidebar;

