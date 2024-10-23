# Define a simulation
set ns [new Simulator]

# Open the NAM trace file to visualize the simulation
set nf [open stop_wait.nam w]
$ns namtrace-all $nf

# Open the trace file to log the events
set tf [open stop_wait.tr w]
$ns trace-all $tf

# Create two nodes (sender and receiver)
set node1 [$ns node]   ;# Sender node
set node2 [$ns node]   ;# Receiver node

# Create a duplex link between the sender and receiver
$ns duplex-link $node1 $node2 1Mb 10ms DropTail

# Setup queue monitoring (optional)
$ns queue-limit $node1 $node2 50

# Set up TCP agent (Stop-and-Wait simulation)
set tcp [new Agent/TCP]
$tcp set window_ 1          ;# Set TCP window to 1 to mimic Stop-and-Wait behavior
$ns attach-agent $node1 $tcp

# Set up TCP sink (receiver) to receive packets from TCP agent
set sink [new Agent/TCPSink]
$ns attach-agent $node2 $sink

# Connect the TCP agent with the TCP Sink
$ns connect $tcp $sink

# Create FTP traffic and attach it to TCP agent
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

# Start FTP traffic at time 0.1 seconds
$ns at 0.1 "$ftp start"

# Schedule to stop FTP at time 4.0 seconds
$ns at 4.0 "$ftp stop"

# Procedure to end the simulation
proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam stop_wait.nam &
    exit 0
}

# Schedule the finish procedure at 5.0 seconds
$ns at 5.0 "finish"

# Run the simulation
$ns run
