#!/usr/bin/env ruby

require 'rubygems'
require 'twitter'

def is_printable? s
    s.each_byte {|x| return false if x < 32 or x > 126}
end

def main
    if ARGV.length < 1
        puts "Usage: #{__FILE__} <twitter_username> [-d delay in seconds]"
        exit
    end

    puts "#{__FILE__} online"
    $last_tweet = nil
    twit_source = ARGV[0]
    delay = (ARGV.length == 3 and ARGV[1] == "-d") ? ARGV[2].to_i : 900

    f = File.open("twitjustice.log","a")

    loop{
        begin
            #latest = `curl http://192.168.1.11:4567/inquirerdotnet 2>/dev/null`
            latest = Twitter.user_timeline(twit_source).first.text
            if $last_tweet != latest and latest.length <= 140
                if is_printable? latest
                    f.syswrite(latest.to_s+"\n")
                    `say -v Alex "#{latest.to_s}"`
                    $last_tweet = latest
                end
            end
            puts "waiting for next in #{delay} seconds"
            sleep delay
            next
        rescue 
            puts "error. retrying in #{delay} seconds"
            sleep delay
            retry
        ensure
            f.close unless f.nil?
        end
    }
end

main() if __FILE__ == $0
