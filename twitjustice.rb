#!/usr/bin/ruby

puts 'twitcaster online'
$last_tweet = nil
loop{
	begin
		latest = `curl http://192.168.1.11:4567/inquirerdotnet 2>/dev/null`
		if $last_tweet != latest and latest.length <= 140
			puts latest.to_s
			`say -v Alex "#{latest.to_s}"`
			$last_tweet = latest
		end
		puts "waiting for next"
		sleep 900
		next
	rescue 
		puts 'retrying'
		retry
	end
}

