//
// Copyright (C) 2004 Andras Varga
// Copyright (C) 2000 Institut fuer Telematik, Universitaet Karlsruhe
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program; if not, see <http://www.gnu.org/licenses/>.
//

package inet.networklayer.ipv4;

import inet.common.MessageDispatcher;
import inet.networklayer.contract.IArp;
import inet.networklayer.configurator.ipv4.Ipv4NodeConfigurator;
import inet.networklayer.contract.INetworkLayer;


//
// Network layer of an Ipv4 node.
//
//
module Ipv4NetworkLayer like INetworkLayer
{
    parameters:
        bool proxyARP = default(true);
        bool forwarding = default(false);
        bool multicastForwarding = default(false);
        string igmpType = default("Igmpv2");
        string arpType = default("Arp");
        string interfaceTableModule;
        *.forwarding = forwarding;
        *.multicastForwarding = multicastForwarding;
        *.interfaceTableModule = default(absPath(interfaceTableModule));
        *.routingTableModule = default(absPath(".routingTable"));
        *.arpModule = default(absPath(".arp"));
        *.icmpModule = default(absPath(".icmp"));
        arp.respondToProxyARP = proxyARP;
        @display("i=block/fork");

    gates:
        input ifIn @labels(INetworkHeader);
        output ifOut @labels(INetworkHeader);
        input transportIn @labels(Ipv4ControlInfo/down);
        output transportOut @labels(Ipv4ControlInfo/up);
        input igmpIn;
        output igmpOut;

    submodules:
        configurator: Ipv4NodeConfigurator {
            parameters:
                @display("p=100,100;is=s");
        }
        routingTable: Ipv4RoutingTable {
            parameters:
                @display("p=100,200;is=s");
        }
        up: MessageDispatcher {
            parameters:
                @display("p=450,100;b=480,5");
        }
        igmp: <igmpType> like IIgmp {
            parameters:
                @display("p=300,200");
        }
        icmp: Icmp {
            parameters:
                @display("p=600,200");
        }
        mp: MessageDispatcher {
            parameters:
                @display("p=450,300;b=480,5");
        }
        ip: Ipv4 {
            parameters:
                useProxyARP = true; // as routes with unspecified next-hop addr are quite common
                @display("p=450,400;q=queue");
        }
        arp: <arpType> like IArp {
            parameters:
                @display("p=300,400;q=pendingQueue");
        }
        lp: MessageDispatcher {
            parameters:
                @display("p=450,500;b=480,5");
        }

    connections allowunconnected:
        transportIn --> { @display("m=n"); } --> up.in++;
        transportOut <-- { @display("m=n"); } <-- up.out++;

        up.out++ --> igmp.routerIn;
        up.in++ <-- igmp.routerOut;

        up.out++ --> mp.in++;
        up.in++ <-- mp.out++;

        up.out++ --> icmp.transportIn;
        up.in++ <-- icmp.transportOut;

        igmp.ipOut --> mp.in++;
        igmp.ipIn <-- mp.out++;

        icmp.ipOut --> mp.in++;
        icmp.ipIn <-- mp.out++;

        mp.out++ --> ip.transportIn;
        mp.in++ <-- ip.transportOut;

        arp.ifOut --> lp.in++;
        arp.ifIn <-- lp.out++;

        ip.queueOut --> lp.in++;
        ip.queueIn <-- lp.out++;

        lp.out++ --> { @display("m=s"); } --> ifOut;
        lp.in++ <-- { @display("m=s"); } <-- ifIn;
}